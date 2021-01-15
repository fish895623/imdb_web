# %% [markdown]
import re


from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.datasets import imdb
from tensorflow.keras.layers import GRU, Dense, Embedding
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


class learning_imdb:
    def __init__(
        self, file: str = "GRU_model.h5", vocab_size: int = 10000, max_len=500
    ):
        """
        file: str
            model filename
        vocab_size: int
            vacab size to numbering
        max_len:
            max length on imdb review

        """
        self.file = file
        self.vocab_size = vocab_size
        self.max_len = max_len

        self.word_to_index = imdb.get_word_index()
        self.loaded_model = load_model(file)
        (self.X_train, self.y_train), (self.X_test, self.y_test) = imdb.load_data()
        pass

    def create_model(self):
        word_to_index = imdb.get_word_index()
        index_to_word = {}
        for key, value in word_to_index.items():
            index_to_word[value + 3] = key

        (self.X_train, self.y_train), (self.X_test, self.y_test) = imdb.load_data(
            num_words=self.vocab_size
        )
        self.X_train = pad_sequences(sequences=self.X_train, maxlen=self.max_len)
        self.X_test = pad_sequences(sequences=self.X_test, maxlen=self.max_len)
        model = Sequential()
        model.add(Embedding(input_dim=self.vocab_size, output_dim=100))
        model.add(GRU(units=128))
        model.add(Dense(units=1, activation="sigmoid"))

        es = EarlyStopping(monitor="val_loss", mode="min", verbose=1, patience=4)
        mc = ModelCheckpoint(
            filepath=self.file,
            monitor="val_acc",
            mode="max",
            verbose=1,
            save_best_only=True,
        )
        model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])
        model.fit(
            x=self.X_train,
            y=self.y_train,
            epochs=15,
            callbacks=[es, mc],
            batch_size=60,
            validation_split=0.2,
        )
        pass

    def sentiment_predict(self, new_sentence):
        # loaded_model = load_model("GRU_model.h5")
        # 알파벳과 숫자를 제외하고 모두 제거 및 알파벳 소문자화
        new_sentence = re.sub("[^0-9a-zA-Z ]", "", new_sentence).lower()

        # 정수 인코딩
        encoded = []
        for word in new_sentence.split():
            # 단어 집합의 크기를 10,000으로 제한.
            try:
                if self.word_to_index[word] <= self.vocab_size:
                    encoded.append(self.word_to_index[word] + 3)
                else:
                    # 10,000 이상의 숫자는 <unk> 토큰으로 취급.
                    encoded.append(2)
            # 단어 집합에 없는 단어는 <unk> 토큰으로 취급.
            except KeyError:
                encoded.append(2)

        pad_new = pad_sequences([encoded], maxlen=self.max_len)  # 패딩
        score = float(self.loaded_model.predict(pad_new))  # 예측
        if score > 0.5:
            return "{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100)
        else:
            return "{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100)


a = "This movie was just way too overrated. The fighting was not professional and in slow motion. I was expecting more from a 200 million budget movie. The little sister of T.Challa was just trying too hard to be funny. The story was really dumb as well. Don't watch this movie if you are going because others say its great unless you are a Black Panther fan or Marvels fan."
