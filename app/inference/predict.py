class Predict:
    data: None
    model: None

    def prediction(data, model):
        prediction = model.predict(data)
        prediction = round(prediction[0], 5)

        return prediction
