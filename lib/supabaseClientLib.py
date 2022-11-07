from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

#
# class SupabaseClient:
#     def __init__(self):
#         self.supabase = self.getSupabase()
#
#     def getSupabase(self):
#         API_URL = os.getenv("API_URL")
#         API_KEY = os.getenv("API_KEY")
#         supabase = create_client(API_URL, API_KEY)
#
#         return supabase

def supabaseClient():
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")
    supabase = create_client(API_URL, API_KEY)

    return supabase
