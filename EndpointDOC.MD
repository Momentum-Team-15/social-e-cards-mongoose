Documentation for endpoints

/cards/

POST request

fields required: 
{
    "user": "<pk>",
	"title": "textfield",
	"card_msg": "textfield",
	"color": "COLOR",
	"font_color": "COLOR"
}

--------------

/cards/

GET request

example response

[
	{
		"title": "Christmas",
		"user": 1,
		"font_color": "GOLD",
		"color": "RED",
		"card_msg": "Happy holidays",
		"created_at": "2022-11-17T21:13:46.461813Z",
		"updated_at": "2022-11-17T21:13:46.461843Z",
		"published": false
	}
]

-----------------

/auth/token/login/

POST Request

fields required:
{
    "password": "",
    "username": ""
}


----------

cards/favorite

POST request

fields required:
{
	"card": "<pk>"
}

GET request

{
	"card": <pk>,
	"created_at": "",
	"user": <pk>
}
----------------

users/friend

POST request

fields required:
{
	"friend":"<pk>"
}

GET request:
{
	"friend":"<pk>"
}