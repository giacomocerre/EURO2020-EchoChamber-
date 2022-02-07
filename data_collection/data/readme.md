# DATA FOLDER
Contiene tre file quali:
- `data_complete.json`
- `final_user_classification.json`
- `hashtags_classification.json`


## `data_complete.json`
Contiene tutti i tweet estratti.
La struttura di un tweet è la seguente:
```
{
    "tweet_id": string,
    "user": string,
    "date": string,
    "text": string,
    "hashtags": string[],
    "mentions": [],
    "retweets": [],
    "reply_to": [],
    "quote_to": [],
    "followers": number,
    "following": number,
    "tweets": number,
    "tweet_classification": number,
    "user_classification": float,
    "vip": boolean
}
```

## `final_user_classification.json`
Contiene tutti gli utenti dei tweet estratti con la loro relativa classificazione, basata sul file `hashtags_classification.json`

## `hashtags_classification.json`
Contiene tutti gli hashtag dei tweet estratti con la loro relativa classificazione.
Ad ogni hashtag presente nel dataset èstato associato un valore numerico: 
- ±3 se l’hashtag esprime una posizione nettamente contraria (+)/nettamente a favore(−) al gesto dell’inginocchiarsi, 
- ±1 se l’hashtag è significativo in quanto vicino ai motivi della fazione contraria (+)/a favore(−) del gesto, ma non specifico sulla questione “inginocchiarsi"
- 0 per gli hashtag neutri e/o non rilevanti.


