Can fully connected feed-forward neural network ever learn y=x^2 dependece (with any number of neurons and any number of layers)?

The dataset which is exactly y=x^2:
<br/>
<img width="677" alt="Screenshot 2024-01-16 at 3 02 23 PM" src="https://github.com/MilanApegaonkar/Python-Modeler/assets/34775146/d3371d70-ef22-429c-a74a-b6c9a3bba092">
<br/>




Chat-GPT suggested model:
<br/>
<img width="666" alt="Screenshot 2024-01-16 at 3 03 34 PM" src="https://github.com/MilanApegaonkar/Python-Modeler/assets/34775146/5cb84c81-79c7-4333-9472-f5f0359eca6e">

<br/>



I dervied all the equations of this neural network once its trained by getting weights and biases:
using below logic:
<br/>
<img width="822" alt="Screenshot 2024-01-16 at 3 11 58 PM" src="https://github.com/MilanApegaonkar/Python-Modeler/assets/34775146/0f27af6b-b2af-43ae-8ca9-6c6a4c9bed25">






layer1 equations:
['-0.010977978*x+-0.07914563', '0.77259254*x+-2.523', '1.2160325*x+-1.8026854', '-1.4869308*x+-4.3064227', '-1.9978771*x+-1.7260332', '1.0154861*x+-2.3848588', '1.3893294*x+-0.9156931', '0.3084059*x+1.2171052', '0.018219909*x+-0.11292136', '0.9471697*x+-3.93977']
<br/>
[neuron1 linear part         , neuron2 linear part  ,................................]

n1=relu(neuron1 linear part)

layer2 equation linear part:
-0.059853982*n1+2.3632672*n2+1.3517455*n3+2.7471404*n4+1.9495982*n5+1.7910599*n6+1.4368546*n7+0.5300105*n8+-0.20618692*n9+1.8067675*n10+-0.43944842

If I consider the value of x = 30 then expected value of y should be 900
but if I plug in x in layer1 equations:
<br/>
<img width="278" alt="Screenshot 2024-01-16 at 3 14 52 PM" src="https://github.com/MilanApegaonkar/Python-Modeler/assets/34775146/afada9cf-0eee-454f-a1f2-19f8649fc9a7">
<br/>





then using this values if I plug it in layer2 equation then the value I get is 253.79483469338047 

Same I get when I do:
<br/>
<img width="541" alt="Screenshot 2024-01-16 at 3 16 32 PM" src="https://github.com/MilanApegaonkar/Python-Modeler/assets/34775146/3c0a6413-d9f6-4c91-bf18-2f8a0b4b0bf7">

<br/>








