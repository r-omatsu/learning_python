<?php

for ($i = 0; $i < 100000; $i++) {
    $a['a' . $i] = true;
    $b[] = 'a' . $i;
}

$time_start = microtime(true);

// array_flip($a);
for ($i = 0; $i < 1000; $i++) {
    // isset($a['a50000']);
    // in_array('a50000', $b);
    isset(array_flip($b)['a50000']);
}

$time = microtime(true) - $time_start;
echo "{$time} 秒";
