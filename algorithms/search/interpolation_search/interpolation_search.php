<?php

function search($arr, $low, $high, $key){
    if($low <= $high && $key >= $arr[$low] && $key <= $arr[$high]) {
        $idx = (int)($low + (((double)($high - $low) / ($arr[$high] - $arr[$low])) * ($key - $arr[$low])));

        if ($arr[$idx] == $key)
            return $idx;

        // If key is larger, key is in right sub array
        if ($arr[$idx] < $key)
            return search($arr, $idx + 1, $high, $key);

        // If key is smaller, key is in left sub array
        if ($arr[$idx] > $key)
            return search($arr, $low, $idx - 1, $key);
    }
    return -1;
}

function result($idx){
    if($idx == -1)
        echo "Element not found \n";
    else
        echo "Element found at index $idx \n";
}

$arr = [11, 12, 14, 17, 19, 20, 21, 22, 25, 34, 36, 42, 47];
$n = sizeof($arr) - 1;
result(search($arr, 0, $n, 23));
result(search($arr, 0, $n, 11));
result(search($arr, 0, $n, 22));
result(search($arr, 0, $n, 47));

?>