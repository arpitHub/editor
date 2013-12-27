<?php

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of getContents
 *
 * @author agile
 */
class getContents {
    
    const DIR_PATH = "/../hashed/";
    
    function __construct($request) {
        $this->user = $request['user'];
    }
    
    function getFolderContents() {
        $path = $this->directory();
        $dirList = scandir($path);
        echo implode("{%}", $this->sohniKardoList($dirList));
    }

    function directory() {
        $path = __DIR__ . self::DIR_PATH . md5($this->user);
        if (is_dir($path)) {
        } else {
            mkdir($path, 777);
        }

        return $path;
    }

    function sohniKardoList($list)
    {
        return array_diff($list, array(".", ".."));
    }
}

$obj = new getContents($_GET);
return $obj->getFolderContents();

?>
