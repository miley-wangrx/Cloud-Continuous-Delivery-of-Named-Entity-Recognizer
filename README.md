[![Python Application test with GitHub actions](https://github.com/miley-wangrx/microservice/actions/workflows/main.yml/badge.svg)](https://github.com/miley-wangrx/microservice/actions/workflows/main.yml)

# Microservice
## Brief
This is a mini project of IDS721, in this project, a microserver was implemented, which can be used as a named entity recognizer. The recognizer will locate and named entities mentioned in the input sentence and classsify them into pre-defined categories such as person names, organizations, locations, time expressions, quantities, monetary values, percentages, etc.

Welcome to click [this link](https://dvk2iniydi.us-east-1.awsapprunner.com) and play with it!

## Demo
Here is a quick walkthrough:


## Features
* The Microservice was built using Fast API
* Used GitHub Actions as Build System to deploy changes
    ![image](https://user-images.githubusercontent.com/88390268/151729808-a31c2a52-c8ae-43a7-aad0-fb705dbfdefb.png)
* Used IaC to deploy code on AWS Cloud9
* The project was deployed on AWS App Runner
    ![image](https://user-images.githubusercontent.com/88390268/151730139-cb1b3282-1b51-4a6b-b643-76a001d94288.png)

## Examples:
### Example 1:
* Sentence: `Biden won the election in year 2020.`
* Output: 
    ![image](https://user-images.githubusercontent.com/88390268/151730818-44830dc0-6b2a-4a82-bf09-3a89c598c9e8.png)

### Example 2:
* Sentence: `Study at Duke University costs 60000 dollars per year`
* Output: 
    ![image](https://user-images.githubusercontent.com/88390268/151730854-542c5fed-13e9-4da7-8462-cd679347fc4b.png)

### Example 3:
* Sentence: `Microsoft will acquire Activision Blizzard for $95.00 per share, in an all-cash transaction valued at $68.7 billion, inclusive of Activision Blizzard’s net cash.`
* Output:  
    ![image](https://user-images.githubusercontent.com/88390268/151731064-d3bee526-b02d-4281-b0a7-18252d6bb2de.png)


