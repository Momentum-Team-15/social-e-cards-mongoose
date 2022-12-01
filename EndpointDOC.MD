Documentation for endpoints

deploy url: https://mongoosesocial.onrender.com

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

GET request
example response
{
	"title": "Christmas card",
	"user": 1,
	"font_color": "GREEN",
	"color": "BLUE",
	"card_msg": "This card has been updated",
	"created_at": "2022-11-20T19:22:01.797201Z",
	"updated_at": "2022-11-29T23:58:04.595171Z",
	"published": false,
	"text_alignment": "1",
	"comments": []
},
----------------
cards/favorite/add

POST
{
	"card":"<pk>"
}

GET
example response
{
	"card": 2,
	"created_at": "2022-11-30T23:50:38.722017Z",
	"user": 17
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

---------------

auth/users/ 

GET request 

{
		"email": "",
		"id": 1,
		"username": "admin"
	}
]

Post Request

{
	"username":"This field is required.",
	"password": "This field is required."
}

----------------

/auth/users/me/

GET Request 

    "email": "",
    "id": 1,
    "username": "admin"

-------

/cards/me

GET 

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
----------------------------------------------------------------
/cards/<pk>
:GET, PATCH, PUT, DELETE

GET
{
	"title": "",
	"user": <userPk>,
	"font_color": "BLACK",
	"color": "WHITE",
	"card_msg": "",
	"created_at": "2022-11-20T19:22:01.797201Z",
	"updated_at": "2022-11-29T22:31:01.906774Z",
	"published": false,
	"text_alignment": "1",
	"comments": []
}
PATCH(Just put whih field you want to update in.)Ex:
{
	"card_msg":"This is a new card message",
}
DELETE
{

}
PUT(Similar to PATCH but you have to rebuild the entire card)
(required fields):
{
	"title":"",
	"text_alignment":"",
	"comments":""
	
}
----------------------------------------------------------------
/users/create
POST
{
	"username": "",
	"password": "",
	"name": "",
	"bio": ""
}

/users/<pk>
:GET, PATCH, PUT, DELETE

GET
{
	"name": "Steve",
	"bio": null,
	"username": ""
}
PATCH
{
	"bio": "This is a new bio"
}
PUT
(only username is required)
{
	"username": "New Username",
	"bio":"This is the same bio",
	"name":"This is the same name"
}
---------------------------------------------------------
/comments/

GET

{
    "pk": "",
    "comment_owner": "", 
    "card": "",
}

POST

{
    "pk": "1",
    "comment_owner": "Hatice", 
    "card": "1",
    "text": "Test a comment"
}

