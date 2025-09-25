import pandas as pd
import hashlib

def hash_to_int(hash_string):
    return int(hashlib.sha256(hash_string.encode("utf-8")).hexdigest(), 16) % (10**8)


cidades_map = {
    "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b": "São Paulo",
    "50e9a8665b62c8d68bccc77c7c92431a1aa26ccbd38ed4bba8dd7422a3a4ab70": "Rio de Janeiro",
    "10e4e7caf8b078429bb1c80b1a10118ac6f963eff098fd25a66c78862ae5ebce": "Belo Horizonte",
    "e6d41d208672a4e50b86d959f4a6254975e6fb9b0881166af52c9fe3b5825de2": "Curitiba",
    "7688b6ef52555962d008fff894223582c484517cea7da49ee67800adc7fc8866": "Brasília",
    "8c1f1046219ddd216a023f792356ddf127fce372a72ec9b4cdac989ee5b0b455": "Salvador",
    "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce": "Porto Alegre",
    "d6acb3c1a79e57bcc03d976cb4d98f56edccd4cf426392e8cd4b01b965ab808b": "Fortaleza",
    "aa4b83bd033762a4": "Recife", 
    "23765fc69c4e3c0b10f5d15471dc2245e2a19af16b513f85aa4b83bd033762a4": "Recife",
    "d26eae87829adde551bf4b852f9da6b8c3c2db9b65b8b68870632a2db5f53e00": "Campinas",
    "482d9673cfee5de391f97fde4d1c84f9f8d6f2cf0784fcffb958b4032de7236c": "Ribeirão Preto",
    "2fca346db656187102ce806ac732e06a62df0dbb2829e511a770556d398e1a6e": "Goiânia",
    "be47addbcb8f60566a3d7fd5a36f8195798e2848b368195d9a5d20e007c59a0c": "Uberlândia",
    "6b51d431df5d7f141cbececcf79edf3dd861c3b4069f0b11661a3eefacbba918": "Florianópolis",
    "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce": "Curitiba",
    "90b5bc7f03c840b2efddb22ffdfc37dd12cb391b49aa0fc8751726c04d32ff30": "Vitória",
    "f6103ca1e01bd200a9258a366b7e8c22a542e771bf11a0679967a5bb47ef3688": "Vila Velha",
    "20ca98162ba780883712eb701c84e4c06f73aba78e903935a9ad799193b4627f": "Campinas",
    "a77b6cbdf6fae1676369dea1e1ea675e4c2400c9e43bd535fdfd9395cb48cbaa": "São José dos Campos",
    "fbb2a73b0bacf3953186a92029e3e9b130373a9ff1449407e6125b3481f4f0ca": "Rio de Janeiro",
    "a8fd7dc0e1bf71874f7bae013d89b07da30f44bdb001c6e44071388ce6fa380f": "São Paulo",
    "df156e8465ff477c90a1393a0ab5947e448ed696ac0d3ea982480f5c237a29e1": "Niterói",
    "06b2d82840e43ed8432b3f444de18b57dbe60637c99379c708aa8e66de83dbc1": "Santos",
    "2b9449f314bf93145f8122906d8dc56c4ca1f116e6db7ad2768d6f9ade29b31e": "Juiz de Fora",
    "a4ecdd704d258aa841bb3f9a1e3b0cafc59bd88810e542f8e7a0519809d78fe7": "Petrópolis",
    "624b60c58c9d8bfb6ff1886c2fd605d2adeb6ea4da576068201b6c6958ce93f4": "Campinas",
    "5c06e46c5e47cfacad16ce1e37f17c09fdbc7072c567613e0b8112173f688a65": "São José do Rio Preto",
    "7d2371aaf1df1dcb6d0614043748cef2e190b46734cd0b1c48ae6fd337217d6f": "Presidente Prudente",
    "c75cb66ae28d8ebc6eded002c28a8ba0d06d3a78c6b5cbf9b2ade051f0775ac4": "São Carlos",
    "afcf8bc077e68eb94dfe783205f32cabdeead61fd32ff5710947b6111ff2ff77": "Araraquara",
    "811786ad1ae74adfdd20dd0372abaaebc6246e343aebd01da0bfc4c02bf0106c": "Uberaba",
    "ab16ce326c754df41ed00df6f64f7073dcac3e2986bbf8b2a1ce4549b189a0fb": "Divinópolis",
    "81b8a03f97e8787c53fe1a86bda042b6f0de9b0ec9c09357e107c99ba4d6948a": "Juiz de Fora",
    "eb624dbe56eb6620ae62080c10a273cab73ae8eca98ab17b731446a31c79393a": "Ouro Preto",
    "274dfec6e079fb08d6b5771537c54d3f0bd36c64c3d8ed0a4e6d2f201b489274": "Campinas",
    "39fa9ec190eee7b6f4dff1100d6343e10918d044c75eac8f9e9a2596173f80c9": "Ribeirão Preto",
    "9cfd3c755be26b4e1645918e2a64a26e3d851ede421e0b257f783b443bc443d1": "São Carlos",
    "093434a3ee9e0a010bb2c2aae06c2614dd24894062a1caf26718a01e175569b8": "Araraquara",
    "560aa3e6e94314c78236109e209ac79e15e05ec8bf2dcb78300ae65e720edf9e": "Piracicaba",
    "c8c9cad7b920b50f713830b8dc55f59fffbbad98335d9f30e0bca8fab5dfeedd": "Sorocaba",
    "29db0c6782dbd5000559ef4d9e953e300e2b479eed26d887ef3f92b921c06a67": "São José dos Campos",
    "8590ac062555493444893ec5871609dffedf8cf684d93f7533bc52ffc5611dc8": "Taubaté",
    "7e07ae1a0cd3da38f7e619aacacec577992e62944683b47726c201890e98d2a3": "Campos do Jordão",
    "673a620c399f28257798d26d037c352676c031573a2b52b266f5f70f32fec994": "Pouso Alegre",
    "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d": "Poços de Caldas",
}

viacoes_map = {
    "8527a891e224136950ff32ca212b45bc93f69fbb801c3b1ebedac52775f99e61": "Viação Cometa",
    "36ebe205bcdfc499a25e6923f4450fa8d48196ceb4fa0ce077d9d8ec4a36926d": "Viação 1001",
    "ec2e990b934dde55cb87300629cedfc21b15cd28bbcf77d8bbdc55359d7689da": "Expresso do Sul",
    "5f9c4ab08cac7457e9111a30e4664920607ea2c115a1433d7be98e97e64244ca": "Viação Águia Branca",
    "48449a14a4ff7d79bb7a1b6f3d488eba397c36ef25634c111b49baf362511afc": "Viação Itapemirim",
    "1dfacb2ea5a03e0a915999e03b5a56196f1b1664d2f768d1b7eff60ac059789d": "Viação Catarinense",
    "1d0ebea552eb43d0b1e1561f6de8ae92e3de7f1abec52399244d1caed7dbdfa6": "Viação Garcia",
    "3068430da9e4b7a674184035643d9e19af3dc7483e31cc03b35f75268401df77": "Viação Util",
    "35135aaa6cc23891b40cb3f378c53a17a1127210ce60e125ccf03efcfdaec458": "Viação Kaissara",
    "c6f3ac57944a531490cd39902d0f777715fd005efac9a30622d5f5205e7f6894": "Viação Andorinha",
    "96061e92f58e4bdcdee73df36183fe3ac64747c81c26f6c83aada8d2aabb1864": "Viação Eucatur",
    "5d389f5e2e34c6b0bad96581c22cee0be36dcf627cd73af4d4cccacd9ef40cc3": "Viação Guanabara",
    "4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5": "Viação Progresso",
    "dbae772db29058a88f9bd830e957c695347c41b6162a7eb9a9ea13def34be56b": "Viação Penha",
    "b4bbe448fde336bb6a7d7d765f36d3327c772b845e7b54c8282aa08c9775ddd7": "Viação Motta",
    "7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451": "Viação Gontijo",
    "68519a9eca55c68c72658a2a1716aac3788c289859d46d6f5c3f14760fa37c9e": "Viação São Geraldo",
    "71ee45a3c0db9a9865f7313dd3372cf60dca6479d46261f3542eb9346e4a04d6": "Viação Planalto",
    "620c9c332101a5bae955c66ae72268fbcd3972766179522c8deede6a249addb7": "Viação Pássaro Marron",
    "37834f2f25762f23e1f74a531cbe445db73d6765ebe60878a7dfbecd7d4af6e1": "Viação Sampaio",
    "bc52dd634277c4a34a2d6210994a9a5e2ab6d33bb4a3a8963410e00ca6c15a02": "Viação Expresso Brasileiro",
    "a46e37632fa6ca51a13fe39a567b3c23b28c2f47d8af6be9bd63e030e214ba38": "Viação Princesa dos Campos",
    "86e50149658661312a9e0b35558d84f6c6d3da797f552a9657fe0558ca40cdef": "Viação Unida",
}


df = pd.read_csv(r"D:\pedro\Documents\clickBus traduzido completo\df_t.csv") 


df = df.rename(columns={
    "nk_ota_localizer_id": "id_compra_hash",
    "fk_contact": "id_cliente",
    "date_purchase": "data_compra",
    "time_purchase": "hora_compra",
    "place_origin_departure": "origem_ida",
    "place_destination_departure": "destino_ida",
    "place_origin_return": "origem_volta",
    "place_destination_return": "destino_volta",
    "fk_departure_ota_bus_company": "viacao_ida",
    "fk_return_ota_bus_company": "viacao_volta",
    "gmv_success": "valor_total_ticket",
    "total_tickets_quantity_success": "quantidade_passagens"
})


df["id_compra"] = df.index + 1 


df["data_compra"] = pd.to_datetime(df["data_compra"]).dt.date
df = df.drop(columns=["hora_compra"])


df["origem_volta"] = df["origem_volta"].apply(lambda x: "Sem Retorno" if x == "0" else x)
df["destino_volta"] = df["destino_volta"].apply(lambda x: "Sem Retorno" if x == "0" else x)
df["viacao_volta"] = df["viacao_volta"].apply(lambda x: "Sem Retorno" if x == "1" else x)

df["tipo_viagem"] = df.apply(lambda row: "Ida e Volta" if row["origem_volta"] != "Sem Retorno" else "Somente Ida", axis=1)


from hashlib import md5

cidades_lista = [
    "Sao Paulo","Rio de Janeiro","Belo Horizonte","Curitiba","Brasilia","Salvador","Porto Alegre","Fortaleza","Recife","Campinas","Ribeirao Preto","Goiania","Uberlandia","Florianopolis","Vitoria","Vila Velha","Sao Jose dos Campos","Niteroi","Santos","Juiz de Fora","Petropolis","Sao Jose do Rio Preto","Presidente Prudente","Sao Carlos","Araraquara","Uberaba","Divinopolis","Ouro Preto","Campos do Jordao","Pouso Alegre","Pocos de Caldas","Guarulhos","Osasco","Barueri","Bauru","Mogi das Cruzes","Sorocaba","Taubate","Jundiai","Piracicaba"
]

viacoes_lista = [
    "Viacao Cometa","Viacao 1001","Expresso do Sul","Viacao Aguia Branca","Viacao Itapemirim","Viacao Catarinense","Viacao Garcia","Viacao Util","Viacao Kaissara","Viacao Andorinha","Viacao Eucatur","Viacao Guanabara","Viacao Progresso","Viacao Penha","Viacao Motta","Viacao Gontijo","Viacao Sao Geraldo","Viacao Planalto","Viacao Passaro Marron","Viacao Sampaio","Viacao Expresso Brasileiro","Viacao Princesa dos Campos","Viacao Unida"
]

def map_city_deterministic(x):
    if x in ("Sem Retorno", "0", 0):
        return "Sem Retorno"
    if x in cidades_map:
        val = cidades_map[x]
        return (pd.Series([val]).str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8"))[0]
    h = int(md5(str(x).encode("utf-8")).hexdigest()[:8], 16)
    return cidades_lista[h % len(cidades_lista)]

def map_viacao_deterministic(x):
    if x in ("Sem Retorno", "1", 1):
        return "Sem Retorno"
    if x in viacoes_map:
        return viacoes_map[x]
    h = int(md5(str(x).encode("utf-8")).hexdigest()[:8], 16)
    return viacoes_lista[h % len(viacoes_lista)]


for col in ["origem_ida", "destino_ida", "origem_volta", "destino_volta"]:
    df[col] = df[col].apply(map_city_deterministic)

for col in ["viacao_ida", "viacao_volta"]:
    df[col] = df[col].apply(map_viacao_deterministic)


df["id_cliente"] = df["id_cliente"].apply(hash_to_int)


df["ticket_medio"] = (df["valor_total_ticket"] / df["quantidade_passagens"]).round(2)


df["rota_completa"] = df.apply(lambda row: f'{row["origem_ida"]} para {row["destino_ida"]}', axis=1)
df["rota_completa"] = df["rota_completa"].str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")


df = df[[
    "id_compra", "id_cliente", "data_compra", "origem_ida", "destino_ida",
    "origem_volta", "destino_volta", "tipo_viagem", "viacao_ida", "viacao_volta",
    "valor_total_ticket", "quantidade_passagens", "ticket_medio", "rota_completa"
]]

df.to_csv(r"clickBus traduzido completo\clickbus_transformado_1000.csv", index=False)

print("Transformação concluída e arquivo salvo em D:\pedro\Documents\clickBus traduzido completo 500 linhas")
print(df.head())
print(df.info())
