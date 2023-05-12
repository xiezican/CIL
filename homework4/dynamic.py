import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Timeline

data=pd.read_excel(r'gdp_data.xlsx')
#(data.columns)
x=list(data.columns)
y=data.values
year=list(data.index)

timeline=Timeline()

for i in range(len(data)):
    xy=list(zip(x,y[i]))
    xy.sort(key=lambda x:x[1],reverse=False)
    xy=xy[-10:]
    bar=(
        Bar()
        .add_xaxis(xaxis_data=[i[0] for i in xy])
        .add_yaxis(series_name=str(2013+i)+'年地区GDP',y_axis=[i[1] for i in xy])
        .reversal_axis()
        .set_global_opts(title_opts=opts.TitleOpts(title='地区GDP排行榜（%s年）'%(2013+i), subtitle='单位：亿元',pos_left='center',pos_top='top'),
                         legend_opts=opts.LegendOpts(is_show=False),
                         visualmap_opts=opts.VisualMapOpts(
                             is_show=True,pos_top='center',pos_right = 'left', range_color=['blue','yellow','orange'],min_=0,max_=10)
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True,position='right',color='red'))
        )
    timeline.add(bar,year[i]).add_schema(is_auto_play=True,play_interval=800)
timeline.render('各地区GDP排行榜.html')

