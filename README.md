# Simple API Server for CPUchain

For production: https://api.cpuchain.org

## Getting started

We have RESTful API which help you fetch info about CPUchain blockchain and interact with it. This api is fetching data directrly from the full node with addres and transaction indexes enabled.

## Install CPUchain core

Download and install CPUchain Core and start `cpuchaind` with `-txindex -addressindex -timestampindex -spentindex` options.

## How to use it?

First of all you have to create `config.py` file in root of project directory with following content:

```
rid = 'api-server'
cache = 3600  # Cache request for 1 hour
secret = 'Lorem ipsum dolor sit amet.'
endpoint = 'http://rpcuser:rpcpassword@127.0.0.1:19707/'
host = '127.0.0.1'
port = 1234
debug = True
```

Then run 'python app.py` to start, we recommend to use nginx as a reverse proxy for production environment.

Responce have following fields:

`result`: list or object which contains requested data
`error`: this field contains error message in case something went wrong
`id`: api server identifier which is set in `config.py` file

P.s. keep in mind, that all amounts in this API should be in **Satoshis**.

## Methods
--------------

### /info

This method return current info about CPUchain blockchain.

Params: none

Request: https://api.cpuchain.org/info

Responce:
```
{
    "result": {
        "chain": "main",
        "blocks": 3568,
        "headers": 3568,
        "bestblockhash": "a7390c667198e96e88e55965d9af81c27ccc7b858cc3de07b623d6a89da7508d",
        "difficulty": 0.02024649845405542,
        "mediantime": 1570818535,
        "chainwork": "000000000000000000000000000000000000000000000000000000275ae68172",
        "reward": 54734486
    },
    "error": null,
    "id": "api-server"
}
```

### /height/<int:height>

This method return block info by given height.

Params:
`offset`: offset of transactions list (default: 0)
`hash`: return only hash of the block (default: false)

Request: https://api.cpuchain.org/height/172238

Responce:
```
{
   "error":null,
   "id":"api-server",
   "result":{
      "hash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
      "confirmations":172239,
      "strippedsize":276,
      "size":312,
      "weight":1140,
      "height":1,
      "version":536870912,
      "versionHex":"20000000",
      "merkleroot":"1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519",
      "tx":[
         "1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519"
      ],
      "time":1562457601,
      "mediantime":1562457601,
      "nonce":1594491056,
      "bits":"1e3fffff",
      "difficulty":6.103423947912204e-05,
      "chainwork":"0000000000000000000000000000000000000000000000000000000000080000",
      "previousblockhash":"000024d8766043ea0e1c9ad42e7ea4b5fdb459887bd80b8f9756f3d87e128f12",
      "nextblockhash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
      "txcount":1
   }
}
```

### /block/<string:hash>

This method return block info by given hash.

Params:
`offset`: offset of transactions list (default: 0)

Request: https://api.cpuchain.org/block/00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf

Responce:
```
{
   "result":{
      "hash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
      "confirmations":172240,
      "strippedsize":276,
      "size":312,
      "weight":1140,
      "height":1,
      "version":536870912,
      "versionHex":"20000000",
      "merkleroot":"1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519",
      "tx":[
         "1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519"
      ],
      "time":1562457601,
      "mediantime":1562457601,
      "nonce":1594491056,
      "bits":"1e3fffff",
      "difficulty":6.103423947912204e-05,
      "chainwork":"0000000000000000000000000000000000000000000000000000000000080000",
      "previousblockhash":"000024d8766043ea0e1c9ad42e7ea4b5fdb459887bd80b8f9756f3d87e128f12",
      "nextblockhash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
      "txcount":1
   },
   "error":null,
   "id":"api-server"
}
```

### /header/<string:hash>

This method return block header by given hash.

Params: none

Request: https://api.cpuchain.org/header/00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf

Responce:
```
{
   "result":{
      "hash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
      "confirmations":172240,
      "strippedsize":276,
      "size":312,
      "weight":1140,
      "height":1,
      "version":536870912,
      "versionHex":"20000000",
      "merkleroot":"1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519",
      "tx":[
         "1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519"
      ],
      "time":1562457601,
      "mediantime":1562457601,
      "nonce":1594491056,
      "bits":"1e3fffff",
      "difficulty":6.103423947912204e-05,
      "chainwork":"0000000000000000000000000000000000000000000000000000000000080000",
      "previousblockhash":"000024d8766043ea0e1c9ad42e7ea4b5fdb459887bd80b8f9756f3d87e128f12",
      "nextblockhash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
      "txcount":1
   },
   "error":null,
   "id":"api-server"
}
```

### /range/<int:height>

This method return range of blocks staring from certain height.

Params:
`offset`: number of blocks required (default: 30)

Request: https://api.cpuchain.org/range/5

Responce:
```
{
   "error":null,
   "id":"api-server",
   "result":[
      {
         "hash":"00002d74f78dbb50be4361879bdf954ae18b2f81f8dee887e1fb4fc907b25a5b",
         "confirmations":172239,
         "strippedsize":242,
         "size":278,
         "weight":1004,
         "height":5,
         "version":536870912,
         "versionHex":"20000000",
         "merkleroot":"d1c2afa482ea56a6d58d00232c6c0c3cc61132f3223f65210aec3b894ee60435",
         "tx":[
            "d1c2afa482ea56a6d58d00232c6c0c3cc61132f3223f65210aec3b894ee60435"
         ],
         "time":1562457659,
         "mediantime":1562457602,
         "nonce":657732403,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"0000000000000000000000000000000000000000000000000000000000180000",
         "previousblockhash":"0000073f09baae311945a488bd7684499892ef12ab18c3451588058cdf72d73e",
         "nextblockhash":"00001aca5f8d3c49e1a0807fb227c9db3f70bc2f7cb5d2fb2b1a88a34414842f",
         "txcount":1,
         "nethash":22215
      },
      {
         "hash":"0000073f09baae311945a488bd7684499892ef12ab18c3451588058cdf72d73e",
         "confirmations":172240,
         "strippedsize":242,
         "size":278,
         "weight":1004,
         "height":4,
         "version":536870912,
         "versionHex":"20000000",
         "merkleroot":"bf8cf2215e8087f850e9404136e73fce1925bfcd18782abebd3b42f06407559e",
         "tx":[
            "bf8cf2215e8087f850e9404136e73fce1925bfcd18782abebd3b42f06407559e"
         ],
         "time":1562457650,
         "mediantime":1562457602,
         "nonce":503316520,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"0000000000000000000000000000000000000000000000000000000000140000",
         "previousblockhash":"00003bad316a7d1045141dc273eb24f9f0bc7ce192552e55c88a7176fb0714dc",
         "nextblockhash":"00002d74f78dbb50be4361879bdf954ae18b2f81f8dee887e1fb4fc907b25a5b",
         "txcount":1,
         "nethash":20971
      },
      {
         "hash":"00003bad316a7d1045141dc273eb24f9f0bc7ce192552e55c88a7176fb0714dc",
         "confirmations":172241,
         "strippedsize":276,
         "size":312,
         "weight":1140,
         "height":3,
         "version":536870912,
         "versionHex":"20000000",
         "merkleroot":"5c81bf7b7b425e0acd0d83b370053a24de132ba11fd6bc2f17a9e3faf91a47d1",
         "tx":[
            "5c81bf7b7b425e0acd0d83b370053a24de132ba11fd6bc2f17a9e3faf91a47d1"
         ],
         "time":1562457602,
         "mediantime":1562457602,
         "nonce":951101994,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"0000000000000000000000000000000000000000000000000000000000100000",
         "previousblockhash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
         "nextblockhash":"0000073f09baae311945a488bd7684499892ef12ab18c3451588058cdf72d73e",
         "txcount":1,
         "nethash":393216
      },
      {
         "hash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
         "confirmations":172242,
         "strippedsize":276,
         "size":312,
         "weight":1140,
         "height":2,
         "version":536870912,
         "versionHex":"20000000",
         "merkleroot":"4bc87f6b55c5341644a931847e55fe54e302dcc6f10c028e05129ff051c834e2",
         "tx":[
            "4bc87f6b55c5341644a931847e55fe54e302dcc6f10c028e05129ff051c834e2"
         ],
         "time":1562457602,
         "mediantime":1562457601,
         "nonce":1325531360,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"00000000000000000000000000000000000000000000000000000000000c0000",
         "previousblockhash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
         "nextblockhash":"00003bad316a7d1045141dc273eb24f9f0bc7ce192552e55c88a7176fb0714dc",
         "txcount":1,
         "nethash":262144
      },
      {
         "hash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
         "confirmations":172243,
         "strippedsize":276,
         "size":312,
         "weight":1140,
         "height":1,
         "version":536870912,
         "versionHex":"20000000",
         "merkleroot":"1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519",
         "tx":[
            "1e001a09c27489c07fec9430ee22b4fa7b39884a9924a2a43be185436d8a2519"
         ],
         "time":1562457601,
         "mediantime":1562457601,
         "nonce":1594491056,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"0000000000000000000000000000000000000000000000000000000000080000",
         "previousblockhash":"000024d8766043ea0e1c9ad42e7ea4b5fdb459887bd80b8f9756f3d87e128f12",
         "nextblockhash":"00000bb6b3c58a58504d19a93774dc45fd7d0640d84820ced7f3062aad07746c",
         "txcount":1,
         "nethash":262144
      },
      {
         "hash":"000024d8766043ea0e1c9ad42e7ea4b5fdb459887bd80b8f9756f3d87e128f12",
         "confirmations":172244,
         "strippedsize":275,
         "size":275,
         "weight":1100,
         "height":0,
         "version":1,
         "versionHex":"00000001",
         "merkleroot":"843757e79673895b776eea4aad22592ca804b43667a58c1919e36260f1a04690",
         "tx":[
            "843757e79673895b776eea4aad22592ca804b43667a58c1919e36260f1a04690"
         ],
         "time":1562457600,
         "mediantime":1562457600,
         "nonce":597696,
         "bits":"1e3fffff",
         "difficulty":6.103423947912204e-05,
         "chainwork":"0000000000000000000000000000000000000000000000000000000000040000",
         "nextblockhash":"00002c0955d6ef303eef57425dcd882bd60074f2d70d0bf9c546e958bff451bf",
         "txcount":1,
         "nethash":0
      }
   ]
}
```

### /balance/<string:address>

This method return address balance.

Params: none

Request: https://api.cpuchain.org/balance/CPUchainr3zKKzphGcQGAMTJ7m63Yop2mC

Responce:
```
{
   "result":{
      "balance":41837168387240,
      "received":96837168387240,
      "locked":0
   },
   "error":null,
   "id":"api-server"
}
```

### /mempool/<string:address>

This method return address mempool transactions.

Params: none

Request: https://api.cpuchain.org/mempool/CH5AtGquaM3kTjdUxLKWZMcVMdsMWgT8Vg

Responce:
```
{
   "error":null,
   "id":"api-server",
   "result":{
      "tx":[
         {
            "txid":"7eff0c19519ec42ee2b478140df7d5d9ae884a8c585c95c0a2ae6d69dcd3d438",
            "index":0,
            "satoshis":25483924,
            "timestamp":1572901374
         }
      ],
      "txcount":1
   }
}
```

### /unspent/<string:address>

This method return address unspent outputs.

Params:
`amount`: amount which you want to spend (default: 0 will return all utxos)

Request: https://api.cpuchain.org/unspent/CPUchainr3zKKzphGcQGAMTJ7m63Yop2mC

Responce:
```
{
   "result":[
      {
         "txid":"abf0f1abf8dce323bf445e7b159aaf03b3534a604f61ca0c7128c89f13a54d1b",
         "index":0,
         "script":"76a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888ac",
         "value":37385817988976,
         "height":171889
      },
      {
         "txid":"d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4",
         "index":0,
         "script":"76a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888ac",
         "value":4451350398264,
         "height":172394
      }
   ],
   "error":null,
   "id":"api-server"
}
```

### /history/<string:address>

This method return list of address transaction hashes.

Params:
`offset`: offset of transactions list (default: 0)

Request: https://api.cpuchain.org/history/CPUchainr3zKKzphGcQGAMTJ7m63Yop2mC

Responce:
```
{
   "error":null,
   "id":"api-server",
   "result":{
      "tx":[
         "d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4",
         "abf0f1abf8dce323bf445e7b159aaf03b3534a604f61ca0c7128c89f13a54d1b",
         "3b3a8de6156e8aded60b4ce56602cbbc59781dd5915d4cefd5438abd0d1f5c88",
         "4869e8ba27e46f2e5ff36f9e773f0ba6d5b2211b5a91d2a66f4282b66de8bc2b",
         "533a0bab6519894c84fc35b9e86ef8a44216f6dbb1c26518ae7eea59234d1db8"
      ],
      "txcount":5
   }
}
```

### /transaction/<string:hash>

This method return info about transaction.

Params: none

Request: https://api.cpuchain.org/transaction/d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4

Responce:
```
{
   "result":{
      "hex":"02000000040d6d9efdae740c44633a31544f5be9c83b8026f711a854c36631f3b9a5989879100000006b483045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a0121039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699afeffffff72be6490b76ce98c0b50485fe759384b6431c395da972d87a41d6055ae76a0dd000000006a47304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa90121025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82feffffff82b31da2202f8bd4f7ef404333970528f811b27bbb856061beaecbae28c280e0000000006b483045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c0121037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773cfefffffffbec787b2cded743f7f0147d286b3a26618018f544e28755ef95a433b06bf1c7030000006b483045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c7301210354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2bfeffffff0238c528690c0400001976a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888acadb91800000000001976a9146e4f50755c840efa33548d0a57c9f7381b57d05888ac67a10200",
      "txid":"d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4",
      "size":669,
      "version":2,
      "locktime":172391,
      "vin":[
         {
            "txid":"799898a5b9f33166c354a811f726803bc8e95b4f54313a63440c74aefd9e6d0d",
            "vout":16,
            "scriptSig":{
               "asm":"3045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a[ALL] 039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699a",
               "hex":"483045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a0121039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699a"
            },
            "value":1703801,
            "valueSat":17038011088,
            "address":"CNpVY24MPXtXKjHMLc629cpq4iz5hPM3dS",
            "sequence":4294967294,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 45b642e8aa7d35cb5242618b1c304a931cbf03b4 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a91445b642e8aa7d35cb5242618b1c304a931cbf03b488ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CNpVY24MPXtXKjHMLc629cpq4iz5hPM3dS"
               ]
            }
         },
         {
            "txid":"dda076ae55601da4872d97da95c331644b3859e75f48500b8ce96cb79064be72",
            "vout":0,
            "scriptSig":{
               "asm":"304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa9[ALL] 025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82",
               "hex":"47304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa90121025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82"
            },
            "value":436478713,
            "valueSat":4364787134052,
            "address":"CYa2tAo4eAZM593nyvA5sEQ6gMfjbiatKH",
            "sequence":4294967294,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 b0ab7281547a63414b803c723864b166c5691a41 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a914b0ab7281547a63414b803c723864b166c5691a4188ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CYa2tAo4eAZM593nyvA5sEQ6gMfjbiatKH"
               ]
            }
         },
         {
            "txid":"e080c228aecbaebe616085bb7bb211f8280597334340eff7d48b2f20a21db382",
            "vout":0,
            "scriptSig":{
               "asm":"3045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c[ALL] 037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773c",
               "hex":"483045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c0121037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773c"
            },
            "value":6826423,
            "valueSat":68264230106,
            "address":"CTwA4vZGweM48ro9eF36Cp1yj2XgLh4sdJ",
            "sequence":4294967294,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 7dd18d3929cb0bb0bae4175d9999e9b1505bf345 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a9147dd18d3929cb0bb0bae4175d9999e9b1505bf34588ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CTwA4vZGweM48ro9eF36Cp1yj2XgLh4sdJ"
               ]
            }
         },
         {
            "txid":"c7f16bb033a495ef5587e244f5188061263a6b287d14f0f743d7de2c7b78ecfb",
            "vout":3,
            "scriptSig":{
               "asm":"3045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c73[ALL] 0354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2b",
               "hex":"483045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c7301210354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2b"
            },
            "value":126545,
            "valueSat":1265451125,
            "address":"CXCiy43qeHdHNM8Y8TU2z9Va6VxxumZaQw",
            "sequence":4294967294,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 a1aba185e58de2312765d6275fdc56b178ca3e94 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a914a1aba185e58de2312765d6275fdc56b178ca3e9488ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CXCiy43qeHdHNM8Y8TU2z9Va6VxxumZaQw"
               ]
            }
         }
      ],
      "vout":[
         {
            "value":445135039,
            "valueSat":4451350398264,
            "n":0,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 4cec0c819fdc76dc5be7528892bd1c3f3197d3d8 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CPUchainr3zKKzphGcQGAMTJ7m63Yop2mC"
               ]
            }
         },
         {
            "value":162,
            "valueSat":1620397,
            "n":1,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 6e4f50755c840efa33548d0a57c9f7381b57d058 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a9146e4f50755c840efa33548d0a57c9f7381b57d05888ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CSX9uzjHrX8d5dd3h7uwQTfqCKcpQHAeLm"
               ]
            }
         }
      ],
      "blockhash":"0000000d9fc290aa69336ed3619c31e8c6611989d5852db4af33280d5ef33e5e",
      "height":172394,
      "confirmations":977,
      "time":1572841612,
      "blocktime":1572841612,
      "amount":445135201
   },
   "error":null,
   "id":"api-server"
}
```

### /decode/<string:raw>

This method return decoded info about transaction.

Params: none

Request: https://api.cpuchain.org/decode/02000000040d6d9efdae740c44633a31544f5be9c83b8026f711a854c36631f3b9a5989879100000006b483045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a0121039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699afeffffff72be6490b76ce98c0b50485fe759384b6431c395da972d87a41d6055ae76a0dd000000006a47304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa90121025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82feffffff82b31da2202f8bd4f7ef404333970528f811b27bbb856061beaecbae28c280e0000000006b483045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c0121037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773cfefffffffbec787b2cded743f7f0147d286b3a26618018f544e28755ef95a433b06bf1c7030000006b483045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c7301210354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2bfeffffff0238c528690c0400001976a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888acadb91800000000001976a9146e4f50755c840efa33548d0a57c9f7381b57d05888ac67a10200

Responce:
```
{
   "result":{
      "txid":"d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4",
      "hash":"d35cfaf61916069290786749efff5fd47d86d98962147eda69293f34033c39e4",
      "version":2,
      "size":669,
      "vsize":669,
      "locktime":172391,
      "vin":[
         {
            "txid":"799898a5b9f33166c354a811f726803bc8e95b4f54313a63440c74aefd9e6d0d",
            "vout":16,
            "scriptSig":{
               "asm":"3045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a[ALL] 039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699a",
               "hex":"483045022100c13917451e11e8259f26fa996b836c1ad89dd952e79a3b4028af3f214fb104670220069b4eb138dea01d47c662d148524405137956f8abc7318e1220adac06c2be7a0121039ddf4e973c0d32c973f296d1786874661f684dd8bf85da151827ae7c4e67699a"
            },
            "sequence":4294967294
         },
         {
            "txid":"dda076ae55601da4872d97da95c331644b3859e75f48500b8ce96cb79064be72",
            "vout":0,
            "scriptSig":{
               "asm":"304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa9[ALL] 025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82",
               "hex":"47304402206c720de410c98af48a2ef99ef2f59738f413fe0a704cd665c9a81c1d7578c0590220255bdca55a795484526129fd25b39ec3d5247b649d3db3590e6ccd099f8f1aa90121025180b54ba0f01fc649780ed87264aea23f07bc3fe1cd12a173a792099920ac82"
            },
            "sequence":4294967294
         },
         {
            "txid":"e080c228aecbaebe616085bb7bb211f8280597334340eff7d48b2f20a21db382",
            "vout":0,
            "scriptSig":{
               "asm":"3045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c[ALL] 037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773c",
               "hex":"483045022100b769e84ddc4b626bfcec1aab5e3b75ff5bdd8077c7a1dea1cf1191a1200be0da02205f12f3068fd7ef8d39f040a596adf5acb94a11bd055c362ca1a83e38d5d2a27c0121037815f214a02873ecfd6e0de8b8bcb46ce256661e103f42511fda1dbd62e1773c"
            },
            "sequence":4294967294
         },
         {
            "txid":"c7f16bb033a495ef5587e244f5188061263a6b287d14f0f743d7de2c7b78ecfb",
            "vout":3,
            "scriptSig":{
               "asm":"3045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c73[ALL] 0354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2b",
               "hex":"483045022100d06010413f7af4893b1a8254ebc9ac95a81e61122fa341a491b86151ce4a053b02200f5946a687ede1e8d4737756e6ea5977443c8959fd52f34e4fa011d119eb4c7301210354c7ae93915c06e6f64f7469e1fd6ee5cab7c9ef9df9c1f12d1072927cad0e2b"
            },
            "sequence":4294967294
         }
      ],
      "vout":[
         {
            "value":44513.50398264,
            "n":0,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 4cec0c819fdc76dc5be7528892bd1c3f3197d3d8 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a9144cec0c819fdc76dc5be7528892bd1c3f3197d3d888ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CPUchainr3zKKzphGcQGAMTJ7m63Yop2mC"
               ]
            }
         },
         {
            "value":0.01620397,
            "n":1,
            "scriptPubKey":{
               "asm":"OP_DUP OP_HASH160 6e4f50755c840efa33548d0a57c9f7381b57d058 OP_EQUALVERIFY OP_CHECKSIG",
               "hex":"76a9146e4f50755c840efa33548d0a57c9f7381b57d05888ac",
               "reqSigs":1,
               "type":"pubkeyhash",
               "addresses":[
                  "CSX9uzjHrX8d5dd3h7uwQTfqCKcpQHAeLm"
               ]
            }
         }
      ]
   },
   "error":null,
   "id":"api-server"
}
```

### /mempool

This method return info about mempool.

Params: none

Request: https://api.cpuchain.org/mempool

Responce:
```
{
   "result":{
      "size":1,
      "bytes":1403,
      "usage":3392,
      "maxmempool":300000000,
      "mempoolminfee":1e-05,
      "minrelaytxfee":1e-05,
      "tx":[
         "7eff0c19519ec42ee2b478140df7d5d9ae884a8c585c95c0a2ae6d69dcd3d438"
      ]
   },
   "error":null,
   "id":"api-server"
}
```

### /supply

This method return info about current coins supply.

Params: none

Request: https://api.cpuchain.org/supply

Responce:
```
{
   "error":null,
   "id":"api-server",
   "result":{
      "supply":870085000000000,
      "mining":870085000000000,
      "height":174016
   }
}
```

### /fee

This method return recomended transaction fee.

Params: none

Request: https://api.cpuchain.org/fee

Responce:
```
{
   "result":{
      "feerate":420,
      "blocks":6
   },
   "error":null,
   "id":"api-server"
}
```

### /broadcast

This methon broadcast raw signed transaction to CPUchain network.
Keep in mind that you have to user **POST** request for this method!

Params:
`raw`: raw signed transaction

Request: https://api.cpuchain.org/broadcast
`raw`: `01000000010175b5e960976058cd81d62893246b54fd52a0f074ec63c4fafd9f460e779e27010000006b48304502210092ac0108461dec3d90c31781ccac868ebb876a2e09939793581d20d733369c6002207473120c0150e1777ee700da88b833ecfb1805cd629a18d29509fad0d03a97970121021121f5e63f7537a6c8e8881b0c54c5914cd117e775c3be0486205c45eced9117fdffffff0210270000000000001976a9147fd7e409fc303e407a933b3392aa197c66348da688ac880d0100000000001976a914436072406255f648da990ea1fa902cb98c4b6e2088ac00000000`

Responce:
```
{
    "result": "8d0f52a1177c7a954cf4f952532c49c8d55f9437539b544d92f83c14e1929950",
    "error": null,
    "id": "api-server"
}
```

## Credits

ApiServer for CPUchain forked off from https://github.com/MicroBitcoinOrg/ApiServer
