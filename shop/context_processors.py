from decouple import config

def tawk_processor(request):
    return {
        'tawk' : config('SRC')
    }
