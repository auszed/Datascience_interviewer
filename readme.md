# Interviewer  for data science

> [!important]  
> This is a summary of the project; all the information can be found here.

![robot scanning](img/cover.jpg)

## Table of Contents

1. [Introduction](#introduction)
2. [Experimentation](#Experimentation)
3. [App](#App)

## Introduction

The idea is to create an app that allows us to experience the types of questions we will receive in a data science interview.

For that, we prepare a serie of experiments that help us decide, the best prompt.

-----
## Experimentation

### Zero-Shot Prompting  
In this experiment, the model did not behave correctly, requiring further experimentation.  

Here its the notebook:
[001_experiment.ipynb](001_experiment.ipynb)

### Few-Shot Prompting  
For this experiment, we carefully selected the questions to include. While the model generally performed correctly, some inconsistencies remained.  

Here its the notebook:
[002_experiment.ipynb](002_experiment.ipynb)

### Chain of Thought  
We applied a variation of this technique by explicitly structuring our questions to guide the model’s reasoning process. This approach allowed the model to follow a series of logical steps.  

Here its the notebook:
[003_experiment.ipynb](003_experiment.ipynb)

### Generated Knowledge & Maieutic Prompting  
We designed structured questions at an expert-level data science standard, covering specific themes. These questions served as references for further refinement and ensured the model maintained a structured questioning approach.  

Here its the notebook:
[004_experiment.ipynb](004_experiment.ipynb)

### Detailing Thinking  
In this stage, we added final refinements, incorporating `<thinking>` and `<answer>` XML tags. This setup allowed us to observe the model’s reasoning process while maintaining control over its output. By hiding the reasoning step, we ensured that the model would first generate structured thoughts before providing an answer.  

The final iteration of the prompt included several specific elements, such as a JSON example to format the output. Additionally, we enforced a rule preventing the model from generating responses beyond the last question.  

A key observation throughout the experimentation was that attempts to steer the conversation toward unrelated topics appeared to function as intended. However, further analysis is required to assess whether emerging techniques could potentially bypass the model’s security constraints.

Here its the notebook:
[005_experiment.ipynb](005_experiment.ipynb)
-----
## App

IN this case the app its develop using streamlit because it was the faster 
way to create a minimum viable product, so we could test the idea, before launching
the product with complex development.

Here we could find the app

[!app link](https://datascienceinterviewer.streamlit.app/)

-----
## Next Steps


- Experiments with RAG augmentation

- Add a language selection

- Personalize the quantity or the themes the model can select for the question to ask

---

## Authors

* [Hanns Juarez](https://github.com/auszed)
