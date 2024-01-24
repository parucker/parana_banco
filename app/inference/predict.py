from dataclasses import dataclass


@dataclass
class Predict:
    model: None

    def prediction(self, data):
        prediction = self.model.predict(data)
        prediction = round(prediction[0], 5)

        return prediction
