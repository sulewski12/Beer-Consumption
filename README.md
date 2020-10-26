# Beer Consumption

### Project description and motivation

As a huge beer lover I always wondered which factors matter the most while the tiny red blink in peoples' head  turn on: "I feel like drinking beer!".<br>
Finding an appropriate dataset with many factors listed isn't an easy task - that's definitely one of my future projects - to scrap, collect or just simply interview people and create my own dataset that will enable me getting to know my neighbourhood better.<br>
Back to the current project - If you were ever asking yourself what makes people drinking beer, you can definitely find few interesting investigations in my notebook. That's the simple regression problem treated with more advanced ensemble techniques - Stacking and Blending. Having few basic features, the model is predicting the beer consumption that may occur. At the end I "packed" all of that in a simple and eye-catching user interface that can be run in your browser.

### Data description

The dataset I used was taken from https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo.<br>
It was collected in Sao Paulo, Brazil in university area. The respondents were between 18 and 28 years old.<br>
The dataset is described in portuguese, nevertheless it's very explicit and easy to understand, at the beginning of my work with the data and translated it into English.

### EDA, Model implementation and taken steps

A detailed explanation what steps I've taken throughout the project is included within the jupyter notebook.

### User Interface

![UI](https://github.com/sulewski12/Beer-Consumption/blob/main/model/ui_screenshot.png)

The screenshot above depicts user interface I created using simple HTML, CSS and JS code. The idea about the UI creation came up to my mind just before completing the project. I do not treat it as a part of this project, more like a small <u>bonus</u> that helps with interaction with the model. The main part of the script has been written in python using flask library.<br>
You can run the script in your browser, the initial values for each cell are implemented by default, you can change them, click the button at the bottom of the page and get your prediction :)

### Further work and improvements

The only thing that stops me from modifications, improvements and testings of the new ideas on this project is my lack of time. As soon as I find some time, I'll get back to it. Here are some ideas:

- There's still a huge room for improvement when it comes to feature engineering. As we have a datetime format column in a dataset, it's possible to use it for further inspections on the data. I used the month value to see how the beer consumption depends on the month. Similar and much more advanced actions would be possible while including also day in it. I did not experiment much when it comes to new feature creation - the only new feature I came up with was delta temperature. Definitely more in-depth inspections in new features' creation would be priceless, while aiming to improve the final model predictions.
- I did not do hyperparameter tuning at all, so it's more than obvious mentioning it here. That's the first step I would take in order to improve the model. Finding optimal parametres for 6 models, then experimenting with giving them diversed weights would lead to the massive improvements.
- Plotting partial dependence plots could give a great overview on the importance of the features that the model came up with. Model explainability is a technique worth giving a try, especially before experiments with feature engineering.

### Helpful resources

While working on this project I found below mentioned sources very helpful:

- https://www.kaggle.com/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition/notebook
- https://github.com/codebasics/py/tree/master/DataScience/BangloreHomePrices
- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, II Edition, O'Reilly, Aurelien Geron, 2019

<i>October 2020, Paweł Sulewski</i>
