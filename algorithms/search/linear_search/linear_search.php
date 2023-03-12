<?php

function search($arr, $key){
    for($i=0; $i < sizeof($arr); $i++){
        if($arr[$i] == $key){
            return $i;
        }
    }
    return -1;
}

function result($idx){
    if($idx == -1){
        echo "Element not found \n";
    } else {
        echo "Element found at index $idx \n";
    }
}

$arr = [0, 42, 69, 17, -5, 2, 9, 1];
result(search($arr, 3));
result(search($arr, 2));

?>