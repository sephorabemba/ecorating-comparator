# Streamlit Demo: Eco Rating Comparator

This is a Streamlit demo app to compare Eco Rating scores for smartphones.

Smartphone information and global scores come from the Orange website: [here](https://boutique.orange.fr/mobile/mobiles-et-smartphones).

Sub-scores are approximates. They were computed automatically from the progress bars on the Eco Rating pictures.

More about the Eco Rating: [here](https://www.ecoratingdevices.com/).

## What is Eco Rating for smartphones?

Eco Rating scores measure the environmental impact of smartphones on their entire life cycles. They are made available online and in retail shops for a selection of smartphones by a consortium of phone operators including Orange, Telia, Proximus and others. 

### Limitations today 
However, do a quick search and you will soon see a few limitations today:
1. Some partner operators do not display the scores in their online shops.
2. No partner operators allow you to compare smartphones on their Eco Rating scores when browsing for a new phone. This feature is missing to really help customers make the best eco-friendly buying choices easily.
3. The sub-scores are only displayed as progress bars and not as numbers, which makes comparing each sub-criteria even more difficult between phones.

### Solution
Worry no more!

This Streamlit demo is an attempt to solve these limitations. It lets you check how sustainable smartphones are and how they compare with each other easily from different points of view.

You can compare around 30 smartphones.

## About the data

1. All smartphone information and Global Eco Rating scores come from the Orange website. 
2. Sub-scores are approximates. They were pre-computed automatically by converting the progress bars on the Eco Rating pictures into the corresponding numeric sub-scores.

## How to run this demo

You can clone this repo and run the demo with:

```
streamlit run streamlit_app.py
```
