<?php
$dataJSON = file_get_contents("php://input")

$data = json_decode($dataJSON);

$conn = new mysqli("localhost", "fernandi2", "s123194", "fernandi2_db");

$sql = "SELECT alias FROM el_pi";

$rs = $conn->query($sql);
$rs->data_seek(0);
while($row = $rs->fetch_assoc()){
    echo $row['alias'] . '<br>';
}
