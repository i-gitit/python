{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter you name : ramu\n",
      "enter your age45\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "name=input(\"enter you name : \")\n",
    "age=int(input(\"enter your age\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mr/Ms ramu your age will be 95 in year  2069\n"
     ]
    }
   ],
   "source": [
    "\n",
    "now=datetime.datetime.now()\n",
    "curr=now.year\n",
    "year=curr+(95-age)\n",
    "print(\"Mr/Ms \"+name+\" your age will be 95 in year \",year)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
