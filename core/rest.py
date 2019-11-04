from flask_restful import Resource, reqparse
from methods.transaction import Transaction
from methods.general import General
from methods.address import Address
from methods.block import Block
import core.utils as utils
from flask import Response
import requests

def init(api):
	api.add_resource(GetInfo, '/info')
	api.add_resource(BlockByHeight, '/height/<int:height>')
	api.add_resource(HashByHeight, '/hash/<int:height>')
	api.add_resource(BlockByHash, '/block/<string:bhash>')
	api.add_resource(BlockHeader, '/header/<string:bhash>')
	api.add_resource(BlocksByRange, '/range/<int:height>')
	api.add_resource(AddressBalance, '/balance/<string:address>')
	api.add_resource(AddressMempool, '/mempool/<string:address>')
	api.add_resource(AddressUnspent, '/unspent/<string:address>')
	api.add_resource(AddressHistory, '/history/<string:address>')
	api.add_resource(TransactionInfo, '/transaction/<string:thash>')
	api.add_resource(DecodeRawTx, '/decode/<string:raw>')
	api.add_resource(MempoolInfo, '/mempool')
	api.add_resource(SupplyPlain, '/supply/plain')
	api.add_resource(Supply, '/supply')
	api.add_resource(EstimateFee, '/fee')
	api.add_resource(Broadcast, '/broadcast')
	api.add_resource(OldChainTx, '/transaction/old/<string:thash>')

class GetInfo(Resource):
	def get(self):
		return General().info()

class BlockByHeight(Resource):
	def get(self, height):
		parser = reqparse.RequestParser()
		parser.add_argument('offset', type=int, default=0)
		args = parser.parse_args()

		data = Block().height(height)
		if data['error'] is None:
			data['result']['tx'] = data['result']['tx'][args['offset']:args['offset'] + 10]

		return data

class HashByHeight(Resource):
	def get(self, height):
		return Block().get(height)

class BlocksByRange(Resource):
	def get(self, height):
		parser = reqparse.RequestParser()
		parser.add_argument('offset', type=int, default=30)
		args = parser.parse_args()

		if args['offset'] > 100:
			args['offset'] = 100

		result = Block().range(height, args['offset'])
		return utils.response(result)

class BlockByHash(Resource):
	def get(self, bhash):
		parser = reqparse.RequestParser()
		parser.add_argument('offset', type=int, default=0)
		args = parser.parse_args()

		data = Block().hash(bhash)
		if data['error'] is None:
			data['result']['tx'] = data['result']['tx'][args['offset']:args['offset'] + 10]

		return data

class BlockHeader(Resource):
	def get(self, bhash):
		data = utils.make_request('getblockheader', [bhash])
		if data['error'] is None:
			data['result']['txcount'] = data['result']['nTx']
			data['result'].pop('nTx')

		return data

class TransactionInfo(Resource):
	def get(self, thash):
		return Transaction().info(thash)

class AddressBalance(Resource):
	def get(self, address):
		return Address().balance(address)

class AddressHistory(Resource):
	def get(self, address):
		parser = reqparse.RequestParser()
		parser.add_argument('offset', type=int, default=0)
		args = parser.parse_args()

		data = Address().history(address)
		if data['error'] is None:
			data['result']['tx'] = data['result']['tx'][args['offset']:args['offset'] + 10]

		return data

class AddressMempool(Resource):
	def get(self, address):
		return Address().mempool(address)

class AddressUnspent(Resource):
	def get(self, address):
		parser = reqparse.RequestParser()
		parser.add_argument('amount', type=int, default=0)
		args = parser.parse_args()

		return Address().unspent(address, args['amount'])

class MempoolInfo(Resource):
	def get(self):
		return General().mempool()

class DecodeRawTx(Resource):
	def get(self, raw):
		return Transaction().decode(raw)

class EstimateFee(Resource):
	def get(self):
		return General().fee()

class Broadcast(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('raw', type=str, default="")
		args = parser.parse_args()

		return Transaction().broadcast(args['raw'])

class Supply(Resource):
	def get(self):
		data = General().supply()
		return utils.response(data)

class SupplyPlain(Resource):
	def get(self):
		data = int(utils.amount(General().supply()['supply']))
		return Response(str(data), mimetype='text/plain')

class OldChainTx(Resource):
	def get(self, thash):
		response = requests.get('http://52.52.107.217:6402/rest/tx/{}.json'.format(thash))

		try:
			return utils.response(response.json())
		except:
			return utils.response(None, {
					'code': 404,
					'message': 'Transaction not found'
				})
