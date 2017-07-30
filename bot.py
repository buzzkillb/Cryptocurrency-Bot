import discord, asyncio, requests

supported_currencies = ["AUD", "BRL", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "KRW", "MXN", "RUB", "TRY", "USD", "BTC", "ETH", "XRP", "LTC", "ETC", "DASH", "XEM", "MIOTA", "XMR", "BTS", "STRAT", "EOS", "ZEC", "BCC", "WAVES"]
not_supperted_text = 'Currency not supported. Supported currencies: USD, AUD, BRL, CAD, CHF, CNY, EUR, GBP, HKD, IDR, INR, JPY, KRW, MXN, RUB, TRY, BTC, ETH, XRP, LTC, ETC, DASH, XEM, MIOTA, XMR, BTS, STRAT, EOS, ZEC, BCC, WAVES'

help_text = '''
Cryptocurrency Commands:
	!btc   - Bitcoin price
	!eth   - Ethereum price
	!xrp   - Ripple price
	!ltc   - Litecoin price
	!etc   - Ethereum Classic price
	!dash  - Dash price
	!xem   - NEM price
	!miota - IOTA price
	!xmr   - Monero price
	!bts   - BitShares price
	!strat - Stratis price
	!eos   - EOS price
	!zec   - Zcash price
	!bcc   - BitConnect price
	!waves - Waves price
Other Commands:
	!api    - Get the API we are using
	!donate - Get our donation address to keep the bot alive
	!github - Get the GitHub address of the project'''

	
def getprice(currency, crypto):
	try:
		if currency.upper() in supported_currencies:
			r = requests.get('https://api.coinmarketcap.com/v1/ticker/' + crypto + '/?convert=' + currency)
			data = r.json()
			price = data[0]['price_' + currency]
			return '1 {} = {} {}'.format(data[0]['name'], str(price), currency.upper())
		else:
			return not_supperted_text
	except:
		return 'Unexpected error'

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as', end = ' ')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('BTC: 1EfEXSdgKWZZ1NzcAxVJGaqmQpW2Hwwx1W')

@client.event
async def on_message(message):

	if message.content.lower().startswith('!btc') or message.content.lower().startswith('!bitcoin'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'bitcoin')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('usd', 'bitcoin')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!eth') or message.content.lower().startswith('!ethereum'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'ethereum')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('usd', 'ethereum')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!xrp') or message.content.lower().startswith('!ripple'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'ripple')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('usd', 'ripple')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!ltc') or message.content.lower().startswith('!litecoin'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'litecoin')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('usd', 'litecoin')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!etc'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'ethereum-classic')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('usd', 'ethereum-classic')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!dash'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'dash')
				await client.send_message(message.channel, price)
			
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'dash')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!xem') or message.content.lower().startswith('!nem'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'nem')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'nem')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!miota') or message.content.lower().startswith('!iota'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'iota')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'iota')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!xmr') or message.content.lower().startswith('!monero'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'monero')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'monero')
			await client.send_message(message.channel, price)						
			
	elif message.content.lower().startswith('!bts') or message.content.lower().startswith('!bitshares'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'bitshares')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'bitshares')
			await client.send_message(message.channel, price)

	elif message.content.lower().startswith('!strat') or message.content.lower().startswith('!stratis'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'stratis')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'stratis')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!eos'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'eos')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'eos')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!zec') or message.content.lower().startswith('!zcash'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'zcash')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'zcash')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!bcc') or message.content.lower().startswith('!bitconnect'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'bitconnect')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'bitconnect')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!waves'):

		try:
		
			if message.content.lower().split()[1]:
				await client.send_typing(message.channel)
				price = getprice(message.content.lower().split()[1].lower(), 'waves')
				await client.send_message(message.channel, price)
				
		except IndexError:
		
			await client.send_typing(message.channel)
			price = getprice('btc', 'waves')
			await client.send_message(message.channel, price)
		
	elif message.content.lower().startswith('!api'):
	
		await client.send_message(message.channel, 'We use CoinMarketCap API.')
		
	elif message.content.lower().startswith('!donate'):
	
		await client.send_message(message.channel, 'You can donate to keep this bot alive.\nBTC Address: 1EfEXSdgKWZZ1NzcAxVJGaqmQpW2Hwwx1W')
	
	elif message.content.lower().startswith('!git') or message.content.lower().startswith('!github'):
	
		await client.send_message(message.channel, 'GitHub: https://github.com/efeaydin06/Cryptocurrency-Bot')
	
	elif message.content.lower().startswith('!help'):
		await client.send_message(message.channel, help_text)

client.run('MzMyOTUzMjczOTMxNzkyMzk0.DEFnAA.vlVF4KN12-J7h7LQZVzYK7YFejg')