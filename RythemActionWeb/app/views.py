from django.shortcuts import get_object_or_404 ,render

from django.http import HttpResponse
from .models import Image
from .models import Post
import markdown
 
def index(request):
    username = "R1N" 
 
    context = {"username": username} 
    return render(request, "app/index.html", context=context) 

# Create your views here.
def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'RythemActionWeb\app\templates\app\index.html', context)

def page_001(request):
    return render(request, 'app/001.html')

def post_detail(request, pk):
  # 該当する記事を取得
  post = get_object_or_404(Post, pk=pk)

  # MarkdownのテキストをHTMLに変換
  # （コードハイライトなどの拡張機能が必要な場合は extensions を追加できます）
  post.content_html = markdown.markdown(
      post.content, extensions=['fenced_code', 'tables']
  )

  return render(request, 'app/post_detail.html', {'post': post})

def post_list(request):
  # データベースからすべてのPostデータを取得（新しい順に並び替える場合などは .order_by('-created_at') も使えます）
  posts = Post.objects.all()

  # テンプレートへデータを渡して描画する
  return render(request, "app/post_list.html", {"posts": posts})