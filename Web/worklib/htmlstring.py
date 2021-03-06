#这里文件定义了常用组合HTML代码的字符串

#排行榜HTML
STRING_HEAD_TITLE_RANKLIST = """<h2><strong>"""
STRING_MID_TITLE_RANKLIST = """</strong></h2>
                <table class="table table-striped table-hover ">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>姓名</th>
                            <th>学院->教学科目</th>
                            <th>赞/不赞 -> 评分</th>
                        </tr>
                    </thead>
                    <tbody>"""
STRING_TAIL_RANKLIST = """</tbody>
                </table>
                """

WORDSTATUS_TABLE_BODY = """<tr><td>2</td><td>加载中...</td><td>加载中...</td><td>加载中...</td></tr><tr class="info"><td>3</td><td>加载中...</td><td>加载中...</td><td>加载中...</td></tr><tr class="success"><td>4</td><td>加载中...</td><td>加载中...</td><td>加载中...</td></tr>"""


#######下面的String是用于曝光台
BP_HEAD_INFO  = """<div class="panel panel-info">
  <div class="panel-heading">
    <h3 class="panel-title">"""

BP_HEAD_NORMAL  = """<div class="panel panel-success">
  <div class="panel-heading">
    <h3 class="panel-title">"""

BP_HEAD_HOT  = """<div class="panel panel-danger">
  <div class="panel-heading">
    <h3 class="panel-title">"""

BP_A_CONTENT  = """</h3>
  </div>
  <div class="panel-body">
      <div class="row" style="margin-left: 10px;margin-right: 10px;">"""

BP_B_DATE = """</div>
    <div class="row" style="text-align: right; margin-right: 12px;">
        <div class="col-md-4">
        <a href="javascript:void(0)" class="btn btn-raised btn-default disabled">"""

BP_C_UPS = """</a>
        </div>
        <div class="col-md-4">
        <a href="javascript:void(0)" class="btn btn-raised btn-default disabled">"""

BP_D_LINK  = """ 人支持</a>
        </div>
        <div class="col-md-4">
        <a href="/badborad/"""

BP_TAIL  = """" class="btn btn-raised btn-primary" target="_blank">阅读更多</a>
    </div>
  </div>
</div></div>"""