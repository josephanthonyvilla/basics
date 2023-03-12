#!/bin/bash

search="binary_search"

echo "Running C"
gcc $search.c -o $search
./$search
echo ""

echo "Running C++"
g++ $search.cpp -o $search
./$search
echo ""

echo "Running C#"
mcs $search.cs
mono $search.exe
echo ""

echo "Running java"
javac $search.java
java $search
echo ""

echo "Running python"
python3 $search.py
echo ""

echo "Running PHP"
php $search.php
echo ""

echo "Running javascript"
node $search.js
echo ""

echo "Running go"
go run $search.go
echo ""

# clean build files
rm $search
rm $search.class
rm $search.exe