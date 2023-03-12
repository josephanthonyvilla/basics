<?php

function search($arr, $key){
    $start = 0;
    $end = count($arr)-1;
    while ($start <= $end) {
        $mid = floor(($start + $end) / 2);
        if ($arr[$mid] == $key) {
            return $mid;
        }
        if ($arr[$mid] < $key) {
            $start = $mid + 1;
        } else {
            $end = $mid - 1;
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

$arr = [-5, 0, 1, 2, 9, 17, 42, 69];
result(search($arr, 3));
result(search($arr, 2));

?>