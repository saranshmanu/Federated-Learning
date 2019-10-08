# Federated Learning

## What is Federated Learning?

Federated Learning is a distributed machine learning approach which enables model training on a large corpus of decentralised data. Federated Learning enables mobile phones to collaboratively learn a shared prediction model while keeping all the training data on device, decoupling the ability to do machine learning from the need to store the data in the cloud. This goes beyond the use of local models that make predictions on mobile devices (like the Mobile Vision API and On-Device Smart Reply) by bringing model training to the device as well.

The goal is a machine learning setting where the goal is to train a high-quality centralised model with training data distributed over a large number of clients each with unreliable and relatively slow network connections.

## How does the application works?

With the rise of many famous libraries like Pysyft and Tensorflow Federated. It has become easier for general developers, researchers and machine learning enthusiasts to create a decentralised machine learning training model.

In this project to train a dataset based on the aim to predict housing prices of the properties listed in the city of Boston, I have used PySyft - a Python library for secure, private Deep Learning. PySyft decouples private data from model training, using Multi-Party Computation (MPC) within PyTorch.

While training the Deep Learning prediction model, the data is securely saved locally with Alice and Bob. For a private training, I used a Federated approach where the ML model is trained locally with ondevice capability of mobile devices owned by two parties Alice and Bob. With the rise of computer performance of the mobile devices, it has become easier to train ML models with much more efficiency.

### Steps involved in the Federated Learning approach

<ol>
<Li> The mobile devices download the global ML model
<Li> Data is being generated while the user is using the application linked with the ML model
<Li> As the user starts to interact with the application more, the user gets much better predictions according to his usage
<Li> Once the model is ready for the scheduled sync with the server. The personalised model that was getting trained with the on device capability is sent to the server
<Li> Models from all the devices are collected and a Federated average function is used to generate a much improved version of the model than the previous one
<Li> Once trained the improved version is sent to all the devices where the user get the experience based on the usage by all the devices around the globe
</ol>

### Resources

<ul>
<li> <a href = "https://github.com/OpenMined/PySyft">More about Pysyft</a>
<li> <a href = "https://arxiv.org/abs/1811.04017">A generic framework for privacy preserving deep learning</a>
<li> <a href = "https://ai.googleblog.com/2017/04/federated-learning-collaborative.html">Federated Learning: Collaborative Machine Learning without Centralized Training Data</a>
<li> <a href = "https://medium.com/@saranshmanu/federated-learning-3097547f8ca3">Tutorial: A new approach of Deep Learning with Federated Learning</a>
</ul>

## Frameworks

<ul>
<Li> Pytorch
<Li> Pysyft
</ul>
