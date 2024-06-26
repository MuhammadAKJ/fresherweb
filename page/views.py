from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'fresher.html')

def install(request):
    response = HttpResponse(content_type='application/bin')
    response['Content-Disposition'] = 'attachment; filename="install.bin"'
    
    file_content = '''
    echo "Installing git..."
    sudo apt-get update > /dev/null
    sudo apt-get install -y git > /dev/null

    echo "Cloning stable FRESHER..."
    git clone -b stable https://github.com/MuhammadAKJ/fresher.git ~/.local/share/fresher > /dev/null

    source ~/.local/share/fresher/install.sh'''
    response.write(file_content)
    return response