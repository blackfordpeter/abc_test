# Peter ABC tech test
This repo contains all the answers to the ABC technical test

## Programming/Scripting
**Using your preferred programming or scripting language, write a function that takes a number as an argument and returns the string "aunty" if that number is divisible by 3 and returns "uncle" otherwise.**

```
#Take the inputNumber and if it is divible by 3 print aunty otherwise print uncle
def auntyUncle(inputNumber):
    '''
        Prints aunty if the inputNumber is divisible by 3 otherwise prints uncle

            Parameters:
                    inputNumber (int): A decimal integer
    '''
    if int(inputNumber) % 3 == 0:
        print "aunty"
    else:
        print "uncle"
```

The script [here](auntyuncle.py) includes some basic handling of inputs. Assuming a python 2 runtime is available execute it
```
chmod +x auntyuncle.py
./auntyuncle.py <input>
```

### Assumptions
- The function will convert the input from a string to an integer
- The full test script will ensure only a single argument is supplied and it it only contains digits before passing it to the function

## Unix/Linux
**Write a command to send the signal SIGTERM to the "mongo" process.**
```
sudo killall mongo
```
**Write a command to recursively delete all files named “virus” in the /usr directory.**

Case sensitive
```
sudo find /usr -name virus -exec rm -rf {} \;
```
Case insensitve
```
sudo find /usr -iname virus -exec rm -rf {} \;
```
## Containers
**Write a Dockerfile that installs the program "curl".**

Dockerfile available [here](Dockerfile)
### Assumptions
- Ubuntu is accepted by the organisation as a base docker image.
- The created image is to be used as a base docker image. (Trying to start this as a container will result in the container dying immedialty)

## Web
**How would you make an HTTP "GET" request with the HTTP "Pragma" request header set to "nocache"?**

Using curl and setting the pragma header
```
curl -H "Pragma: no-cache" https://www.abc.net.au
```