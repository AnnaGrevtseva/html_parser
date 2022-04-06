# Weather


## CLI
With this application, you can get a weather forecast in any city of Russia.
Information is provided by https://world-weather.ru
### Running application
To start the application, the user needs to enter the mandatory ```--city``` 
parameter in any case (lower, upper, capitalize or even camel) in command line (cmd).

For example:
```
>python.exe -m app --city moscow
Current weather in Moscow: -7°
```

##### Requirements
You must have Python 3.8+ to run the application.
External Python Libraries used:
- bs4
- requests
- typer
