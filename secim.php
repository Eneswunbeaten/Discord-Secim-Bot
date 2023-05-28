<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://scdn.ankahaber.net/secimsonuc/site/ikincitur/web/cb-overview.json?v=1685289079494%27');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'authority: scdn.ankahaber.net',
    'accept: application/json',
    'accept-language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6',
    'origin: https://secim.ankahaber.net/',
    'referer: https://secim.ankahaber.net/',
    'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile: ?0',
    'sec-ch-ua-platform: "Windows"',
    'sec-fetch-dest: empty',
    'sec-fetch-mode: cors',
    'sec-fetch-site: same-site',
    'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accept-encoding: gzip',
]);

$response = curl_exec($ch);

curl_close($ch);
echo $response;