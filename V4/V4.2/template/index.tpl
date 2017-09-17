% include('template/header.tpl', title='{{ title }}')
<h1>{{ title }}</h1>
<a href="{{ link1 }}"><img src="{{ mynd1 }}"></a>
<a href="{{ link2 }}"><img src="{{ mynd2 }}"></a>
<a href="{{ link3 }}"><img src="{{ mynd3 }}"></a>
% include('template/footer.tpl', info = '{{ contact }}')