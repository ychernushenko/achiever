def goal():
    out = """
<!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
    <meta name='viewport' content='width=760px, initial-scale=1.0'>
    <link href='../static/css/bootstrap.css' rel="stylesheet" media='screen'>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src='./../assets/js/html5shiv.js'></script>
      <script src='../../assets/js/respond.min.js'></script>
    <![endif]-->
  </head>
  <body>
    <table class='table table-floating'>
        <tbody>
            <tr height='3em' style='background-color: #eee'>
                <th colspan=4><h1 >Dashboard</h1></th>
            </tr>
            <tr><th colspan=4>Mine</th></tr>
            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button class='btn btn-success' >In Progress</button></td>
            </tr>

            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button class='btn btn-success'>In Progress</button></td>
            </tr>

            <tr><th colspan=4>Following</th><tr>
            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button type='button' class='btn btn-success'>In Progress</td>
            </tr>

            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button type='button' class='btn btn-success'>In Progress</td>
            </tr>

            <tr><th colspan=4>Request</th></tr>
            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button type='button' class='btn btn-success'>In Progress</td>
            </tr>

            <tr>
                <td><input type='checkbox' /></td>
                <td>Goal</td>
                <td>Me</td>
                <td><button type='button' class='btn btn-primary'>Follow</button>&nbsp;&nbsp;<button class='btn btn-danger'>Hide</button></td>
            </tr>
        </tbody>
    </table>



    <script src='//code.jquery.com/jquery.js'></script>
    <script src='static/js/bootstrap.min.js'></script>
  </body>
</html>"""
    return out
