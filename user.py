import asyncio
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import DeleteMessagesRequest
from datetime import datetime
from requests import get
import requests
from mbpro import pega


now = datetime.now()

dia = now.day
mes = now.month
ano = now.year


api_id = 968300
api_hash = '6cf0f95aa532b71991144f0aa95fe302'
name = 'botizadu'

client = TelegramClient(name, api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(msg):
	text = msg.raw_text

#await client.send_message('hummmmmnnjnnn', '**Só tô floodando, não me dá spam!**')


	s = requests.Session()
	
	def paste(texto):
		url = 'https://paste.ee/paste'
	
		headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-A505GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'referer': 'https://paste.ee/'}
	
		clear = texto.upper().replace(" ", "+").replace("""
""", "%0D%0A").replace(":", "%3A").replace("Ã", "%C3%83").replace("/", "%2F").replace("Ç", "%C3%87")
		dict = f"""_token=X2aXn3Mu9dCELpxEsBUZMVWKugaLvXekP1Q5N0E4&expiration=2592000&expiration_views=&description=&paste%5Bsection1%5D%5Bname%5D=PASTE+FOR+TELEGRAM&paste%5Bsection1%5D%5Bsyntax%5D=text&paste%5Bsection1%5D%5Bcontents%5D={clear}&fixlines=true&jscheck=validated"""
	
	
		api = s.post(url, headers=headers, data=dict).text
		link = pega(api, '<a class="raw" href="', '"')

		return link
	#--COMANDOS--#
	if(text.lower() == '!cotacao'):
		url = 'https://economia.awesomeapi.com.br/USD'
		cota = get(url).text
		USD = pega(cota, '"high":"', '"')
		valor_dec = float(USD)
		USD_BRL = round(valor_dec, 2)
		await msg.reply(f"**[#] VALOR DO DÓLAR:** `R$ {USD_BRL}`\n**[#] CONSULTADO DIA:** `{dia}/{mes}/{ano}`")
		msgs = await client.get_messages('me')
		#print(msgs)
		result = client.invoke(DeleteMessagesRequest([msgs[0].id]))
		print(result)
	elif(text.lower() == '!comandos'):
		await msg.reply(f"""**[#] COMANDOS:**

!cpf - `CONSULTA DADOS, DÊ UM CPF`
!cotacao - `VÊ A COTAÇÃO, DO DÓLAR`

**[#] ATUALIZADO, DIA:** `19/11/2019`""")
	
	
	if(text.lower().split()[0] == '!cpf' and text.split()[1]):
		cpf = text.replace('!cpf', '').replace('-', '').replace('.', '').replace(' ', '')
		url = 'http://34.67.110.147/TUFOS/cpfaasa.php?list='+cpf
		api = get(url).text
		
		if(api == ''):
			await msg.reply(f"**[#] NÃO ENCONTRADO!!!**")
		else:
			nome_cpf = pega(api, '"Nome":"', '"')
			data_cpf = pega(api, '"dataNasc":" ', ' "').replace("\/", "/")
			mae_cpf = pega(api, '"nomeMae":"', '"')
			idade_cpf = pega(api, '"Idade":"', '"').upper()
			situacao_cpf = pega(api, '"situacao":"', '"')
			paste_e = f"""CPF:
{cpf}
NOME COMPLETO:
{nome_cpf}
DATA DE NASCIMENTO:
{data_cpf}
IDADE:
{idade_cpf}
NOME DA MÃE:
{mae_cpf}
SITUAÇÃO:
{situacao_cpf}"""
			complete = paste(paste_e)
			await msg.reply(f"""**⟬#⟭ CPF:**
`{cpf}`

**⟬#⟭ NOME COMPLETO:**
`{nome_cpf}`

**⟬#⟭ DATA DE NASCIMENTO:**
`{data_cpf}`

**⟬#⟭ NOME DA MÃE:**
`{mae_cpf}`

**⟬#⟭ CLIQUE** [AQUI]({complete}) **PARA VER, OS DADOS COMPLETOS**
""")

	



#print(msg.stringify())

print('[#] INICIADO...')
client.start()
client.run_until_disconnected()