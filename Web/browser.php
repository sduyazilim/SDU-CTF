<?php

$ctfhash =  $_SERVER['HTTP_USER_AGENT'];

if($ctfhash == 'SD-Browser'){
	echo "sduyazilim_{flag_web_ctf_akiyoooooooo}";
	}
else{
	echo "You must use the SD-Browser :(";
}
?>
