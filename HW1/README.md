# Homework1: Tree Christmas tree & Diffie-Hellman key exchange cracker

## Introduce

You need to be familiar with the following topics to get the homework done:
+ Basic python syntax
+ Basic input and output
+ Create python function
+ Usage of for and while loop

In this homework, you will need to design a Christmas tree generator and a function to crack Diffie-Hellman key exchange protocol.

### Christmas Tree Generator
In this part, you will need to design a Christmas tree generator that you can enter a number and generate Christmas trees based on the entered numbers.<br>
If you don’t know what the output Christmas tree looks like, you can use **hw1_example.py** to generate a sample Christmas tree and your generator in your homework must output the same result as sample.

The usage of **hw1_example.py** is as follows:<br>
If you want to produce a 3-layer Christmas tree, you need to enter the following command in the command line environment(ubuntu):
```
$ python3 hw1_example.py 3
               /*\
              /***\
             /*****\
          /***********\
         /*************\
        /***************\
       /*****************\
    /***********************\
   /*************************\
  /************|||************\
 /*************|||*************\
/**************|||**************\
```
If you want to produce a 5-layer Christmas tree, you need to enter the following command in the command line environment(ubuntu):
```
$ python3 hw1_example.py 5
                                  /*\
                                 /***\
                                /*****\
                             /***********\
                            /*************\
                           /***************\
                          /*****************\
                       /***********************\
                      /*************************\
                     /***************************\
                    /*****************************\
                   /*******************************\
               /***************************************\
              /*****************************************\
             /*******************************************\
            /*********************************************\
           /***********************************************\
          /*************************************************\
      /*********************************************************\
     /***********************************************************\
    /****************************|||||****************************\
   /*****************************|||||*****************************\
  /******************************|||@|******************************\
 /*******************************|||||*******************************\
/********************************|||||********************************\
```
The number entered may be very large, and your function must be able to generate a Christmas tree with the correct specifications.

### Diffie-Hellman key exchange cracker
In this part, you need to implement a function to crack Diffie-Hellman key exchange protocol.<br>
In cryptography, there is a security protocol called Diffie-Hellman key exchange, which allows both parties to establish a key through an insecure channel without any prior information. Then, they are able to encrypt their message with this key.

Suppose there are two people, Alice and Bob, who need to send messages between each other.<br>
First of all, they must have to agree on a prime number $p$ and base number $g$, and make it public. Next, Alice and Bob will choose a private number respectively (sometimes called a private key) $a$ and $b$, where $a, b \$, and keep
them so that others will not know.
So Alice doesn’t know what is, and Bob doesn’t know what is.
They will use and to calculate their respective public keys and as the
following method:
