from flask import render_template, request, flash, redirect, session, g, abort
from . import routes

#### INITIAL ROUTES ####
@routes.route("/region/01", methods=["GET"])
def region1_page():
    """single entry page - reroute to that country"""

    return redirect("/alaska")
    
@routes.route("/region/02", methods=["GET"])
def region2_page():
    """single entry page - reroute to that country"""

    return redirect("/canada")

@routes.route("/region/03", methods=["GET"])
def region3_page():


    return render_template('/initial_routes/square03.html')

@routes.route("/region/04", methods=["GET"])
def region4_page():


    return render_template('/initial_routes/square04.html')

@routes.route("/region/05", methods=["GET"])
def region5_page():


    return render_template('/initial_routes/square05.html')

@routes.route("/region/06", methods=["GET"])
def region6_page():


    return render_template('/initial_routes/square06.html')

@routes.route("/region/07", methods=["GET"])
def region7_page():


    return render_template('/initial_routes/square07.html')

@routes.route("/region/08", methods=["GET"])
def region8_page():


    return redirect("/russia")

@routes.route("/region/09", methods=["GET"])
def region9_page():


    return render_template('/initial_routes/square09.html')

@routes.route("/region/10", methods=["GET"])
def region10_page():


    return render_template('/initial_routes/square10.html')

@routes.route("/region/11", methods=["GET"])
def region11_page():


    return render_template('/initial_routes/square11.html')

@routes.route("/region/12", methods=["GET"])
def region12_page():


    return render_template('/initial_routes/square12.html')

@routes.route("/region/13", methods=["GET"])
def region13_page():


    return render_template('/initial_routes/square13.html')

@routes.route("/region/14", methods=["GET"])
def region14_page():


    return redirect("/home")

@routes.route("/region/15", methods=["GET"])
def region15_page():


    return render_template('/initial_routes/square15.html')

@routes.route("/region/16", methods=["GET"])
def region16_page():


    return render_template('/initial_routes/square16.html')
    
@routes.route("/region/17", methods=["GET"])
def region17_page():


    return render_template('/initial_routes/square17.html')

@routes.route("/region/18", methods=["GET"])
def region18_page():


    return render_template('/initial_routes/square18.html')

@routes.route("/region/19", methods=["GET"])
def region19_page():


    return render_template('/initial_routes/square19.html')

@routes.route("/region/20", methods=["GET"])
def region20_page():


    return render_template('/initial_routes/square20.html')

@routes.route("/region/21", methods=["GET"])
def region21_page():


    return render_template('/initial_routes/square21.html')

@routes.route("/region/22", methods=["GET"])
def region22_page():


    return render_template('/initial_routes/square22.html')

@routes.route("/region/23", methods=["GET"])
def region23_page():


    return render_template('/initial_routes/square23.html')

@routes.route("/region/24", methods=["GET"])
def region24_page():


    return render_template('/initial_routes/square24.html')

@routes.route("/region/25", methods=["GET"])
def region25_page():


    return redirect("/home")

@routes.route("/region/26", methods=["GET"])
def region26_page():


    return render_template('/initial_routes/square26.html')

@routes.route("/region/27", methods=["GET"])
def region27_page():


    return render_template('/initial_routes/square27.html')

@routes.route("/region/28", methods=["GET"])
def region28_page():


    return render_template('/initial_routes/square28.html')

@routes.route("/region/29", methods=["GET"])
def region29_page():


    return render_template('/initial_routes/square29.html')

@routes.route("/region/30", methods=["GET"])
def region30_page():


    return redirect("/home")

@routes.route("/region/31", methods=["GET"])
def region31_page():


    return render_template('/initial_routes/square31.html')

@routes.route("/region/32", methods=["GET"])
def region32_page():


    return render_template('/initial_routes/square32.html')
