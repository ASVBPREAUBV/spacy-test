# TESTING SPACY

[getting started spacy](https://spacy.io/usage/) -
[virtualenv docs](https://virtualenv.pypa.io/en/stable/installation/)

## TODO

### Develop

1. Start virtual Enviroment

        source env/bin/activate

2. Run Example
    
        python example.py
    
### Init

    
1. Init virtual Enviroment

    ```virtualenv env```


2. Start virtual Enviroment

    ```source env/bin/activate```

3. At the beginning of the line of you commandline (e.g. bash) should now show (env) up.
    
4. Install dependencies

    ```pip install -r requirements.txt```

5. Install language-pack

    ```python -m spacy download de```
    

#### Remember

- Save installed pip to requirements.txt
   ```
    pip freeze > requirements.txt
    ```