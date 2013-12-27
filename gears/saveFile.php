<?php



class SaveFile
{


    function __construct($user)
    {
        $this->user = $user;
    }

    public function save($fileName, $content)
    {
        $hashed = __DIR__ . "/../hashed/";
        $dir = md5($this->user);

        $fileName = $hashed . $dir . "/" . $fileName;
        try {
            file_put_contents($fileName, $content);
        } catch (\Exception $e) {
            echo $e->getMessage();
        }
    }
}

$saver = new SaveFile($_REQUEST['user']);
$saver->save($_REQUEST['fileName'], $_REQUEST['str']);