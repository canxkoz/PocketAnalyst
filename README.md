## Inspiration

We're all told that stocks are a good way to diversify our investments, but taking the leap into trading stocks is daunting. How do I open a brokerage account? What stocks should I invest in? How can one track their investments? We learned that we were not alone in our apprehensions, and that this problem is even worse in other countries. For example, in Indonesia (Scott's home country), only 0.3% of the population invests in the stock market.

A lack of active retail investor community in the domestic stock market is very problematic. Investment in the stock markets is one of the most important factors that contribute to the economic growth of a country. That is the problem we set out to address. In addition, the ability to invest one's savings can help people and families around the world grow their wealth -- we decided to create a product that makes it easy for those people to make informed, strategic investment decisions, wrapped up in a friendly, conversational interface.

## What It Does

PocketAnalyst is a Facebook messenger and Telegram chatbot that puts the brain of a financial analyst into your pockets, a buddy to help you navigate the investment world with the tap of your keyboard. Considering that two billion people around the world are unbanked, yet many of them have access to cell/smart phones, we see this as a big opportunity to push towards shaping the world into a more egalitarian future.

**Key features:**
- A bespoke investment strategy based on how much risk users opt to take on, based on a short onboarding questionnaire, powered by several AI models and data from Goldman Sachs and Blackrock.
- In-chat brokerage account registration process powered DocuSign's API.
- Stock purchase recommendations based on AI-powered technical analysis, sentiment analysis, and fundamental analysis based on data from Goldman Sachs' API, GIR data set, and IEXFinance.
- Pro-active warning against the purchase of a high-risk and high-beta assets for investors with low risk-tolerance powered by BlackRock's API.
- Beautiful, customized stock status updates, sent straight to users through your messaging platform of choice.
- Well-designed data visualizations for users' stock portfolios.
- In-message trade execution using your brokerage account (proof-of-concept for now, obviously)

## How We Built it

We used multiple LSTM neural networks to conduct both technical analysis on features of stocks and sentiment analysis on news related to particular companies

We used Goldman Sachs' GIR dataset and the Marquee API to conduct fundamental analysis. In addition, we used some of their data in verifying another one of our machine learning models. Goldman Sachs' data also proved invaluable for the creation of customized stock status "cards", sent through messenger.

We used Google Cloud Platform extensively. DialogFlow powered our user-friendly, conversational chatbot. We also utilized GCP's computer engine to help train some of our deep learning models. Various other features, such as the app engine and serverless cloud functions were used for experimentation and testing.  

We also integrated with Blackrock's APIs, primarily for analyzing users' portfolios and calculating the risk score.

We used DocuSign to assist with the paperwork related to brokerage account registration.

## Future Viability

We see a clear path towards making PocketAnalyst a sustainable product that makes a real difference in its users' lives. We see our product as one that will work well in partnership with other businesses, especially brokerage firms, similar to what CreditKarma does with credit card companies. We believe that giving consumers access to a free chatbot to help them invest will make their investment experiences easier, while also freeing up time in financial advisors' days.

## Challenges We Ran Into

Picking the correct parameters/hyperparameters and discerning how our machine learning algorithms will make recommendations in different cases.

Finding the best way to onboard new users and provide a fully-featured experience entirely through conversation with a chatbot.

Figuring out how to get this done, despite us not having access to a consistent internet connection (still love ya tho Cal :D). Still, this hampered our progress on a more-ambitious IOT (w/ google assistant) stretch goal. Oh, well :)


## Accomplishments That We Are Proud Of

We are proud of our decision in combining various Machine Learning techniques in combination with Goldman Sachs' Marquee API (and their global investment research dataset) to create a product that can provide real benefit to people. We're proud of what we created over the past thirty-six hours, and we're proud of everything we learned along the way!

## What We Learned

We learned how to incorporate already existing Machine Learning strategies and combine them to improve our collective accuracy in making predictions for stocks. We learned a ton about the different ways that one can analyze stocks, and we had a great time slotting together all of the different APIs, libraries, and other technologies that we used to make this project a reality.

## What's Next for PocketAnalyst

This isn't the last you've heard from us!

We aim to better fine-tune our stock recommendation algorithm. We believe that are other parameters that were not yet accounted for that can better improve the accuracy of our recommendations; Down the line, we hope to be able to partner with finance professionals to provide more insights that we can incorporate into the algorithm.
