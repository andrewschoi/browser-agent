# Browser agent

## A brief introduction...

Training specialized and performant multi-modal models is hard and expensive, requiring huge server capacities and large amounts of specialized data. Yet, for a large majority of tasks, emerging text-to-text models demonstrate great general ability in being able to understand, learn, and create insights for reasonable scenarios. But so far, they simply don't possess the means to interact with the environment they're in.

This project aims to leverage strong-performing large models and equip them with tools to perform autonomously in the web-browser context.

## Strategy and Approach

Browsers operate visually by converting HTML, CSS, and JavaScript into beautiful webpages. However, the strongest, most reliable language models that are economically available do not accept images as inputs, and it does not take long to realize that it is simply unrealistic to pass the entire html content of a webpage and expect a quality result.

Web automation libraries exist, and plenty of talented engineers have already invested time into making these tools robust. Therefore, this project is primarily interested in boiling down noisy html structure into its core semantics, relying on intuitive heuristics like distance and accessible web design.

... to be continued

## Getting started

```
git clone git@github.com:andrewschoi/browser-agent.git
cd browser-agent
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```
