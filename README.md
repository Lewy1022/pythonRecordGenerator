# RecordGenerator
> Jest to prosty skrypt generujacy dane do bazy danych

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Skrypt jest generatorem danych mającym symulować działanie aplikacji.
Zadaniem generatora jest wygenerowanie w dowolnym momencie dużej liczby wierszy. Generator
działa przyrostowo (kolejne uruchomienie dodaje kolejne wiersze). Skrypt jest przygotowany jago zadanie na studia z przedmiotu aplikacje bazodonowe.


## Screenshots
![Example screenshot](./img/screenshot.png)

## Technologies
* Python 3.8
* cx_oracle


## Setup
1. Należy otworzyć wiersz poleceń i należy zmienić ściężkę do folderu wkórym znajduje się generator.
2. Następnie należy wywołąć komendę w wierszu poleceń:python generator.py <argument1> <argument2> gdzie:
   * <argument1> - jest to nazwa tabeli do, której chemy generowaćinserty. Dostępne wartości:
    - klient
    - trener
    - kontakty
    - cennik
    - cwiczenia
    - plan_treningu
    - Plan_cwiczen
    - Rejestr_wejsc_wyjsc
    - Adresy
   * <argument2> - jest to ilość insertów, które chcemy wygenerować

## Code Examples
Show examples of usage:
`put-your-code-here`

## Features
List of features ready and TODOs for future development
* Awesome feature 1
* Awesome feature 2
* Awesome feature 3

To-do list:
* Wow improvement to be done 1
* Wow improvement to be done 2

## Status
Project is: _in progress_, _finished_, _no longer continue_ and why?

## Inspiration
Add here credits. Project inspired by..., based on...

## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!
