from flask import render_template, request, redirect, session, g, abort
from . import routes
from helpers import get_region_avg
from sqlalchemy import func

#### INITIAL ROUTES ####
@routes.route("/region/01", methods=["GET"])
def region1_page():
    """single entry page - reroute to that country"""
    if not g.user:
        return redirect("/home")

    return redirect("/alaska")
    
@routes.route("/region/02", methods=["GET"])
def region2_page():
    """single entry page - reroute to that country"""
    if not g.user:
        return redirect("/home")

    return redirect("/canada")

@routes.route("/region/03", methods=["GET"])
def region3_page():
    if not g.user:
        return redirect("/home")

    canada_avg=get_region_avg('Canada')
    greenland_avg=get_region_avg('Greenland')
    acrtic_avg=get_region_avg('Arctic Ocean')

    return render_template('/initial_routes/square03.html', canada_avg=canada_avg, greenland_avg=greenland_avg, acrtic_avg=acrtic_avg)

@routes.route("/region/04", methods=["GET"])
def region4_page():
    if not g.user:
        return redirect("/home")

    acrtic_avg=get_region_avg('Arctic Ocean')
    greenland_avg=get_region_avg('Greenland')
    iceland_avg=get_region_avg('Iceland')

    return render_template('/initial_routes/square04.html', iceland_avg=iceland_avg, greenland_avg=greenland_avg, acrtic_avg=acrtic_avg)

@routes.route("/region/05", methods=["GET"])
def region5_page():
    if not g.user:
        return redirect("/home")

    nsea_avg=get_region_avg('North Sea')
    acrtic_avg=get_region_avg('Arctic Ocean')
    russia_avg=get_region_avg('Russia')

    return render_template('/initial_routes/square05.html', nsea_avg=nsea_avg, acrtic_avg=acrtic_avg, russia_avg=russia_avg)

@routes.route("/region/06", methods=["GET"])
def region6_page():
    if not g.user:
        return redirect("/home")
        
    acrtic_avg=get_region_avg('Arctic Ocean')
    russia_avg=get_region_avg('Russia')

    return render_template('/initial_routes/square06.html', acrtic_avg=acrtic_avg, russia_avg=russia_avg)

@routes.route("/region/07", methods=["GET"])
def region7_page():
    if not g.user:
        return redirect("/home")
        
    acrtic_avg=get_region_avg('Arctic Ocean')
    russia_avg=get_region_avg('Russia')

    return render_template('/initial_routes/square07.html', acrtic_avg=acrtic_avg, russia_avg=russia_avg)

@routes.route("/region/08", methods=["GET"])
def region8_page():
    """single entry page - reroute to that country"""
    if not g.user:
        return redirect("/home")
        
    return redirect("/russia")

@routes.route("/region/09", methods=["GET"])
def region9_page():
    if not g.user:
        return redirect("/home")
        
    alaska_avg=get_region_avg('Alaska')
    cali_avg=get_region_avg('California')

    return render_template('/initial_routes/square09.html', alaska_avg=alaska_avg, cali_avg=cali_avg)

@routes.route("/region/10", methods=["GET"])
def region10_page():
    if not g.user:
        return redirect("/home")
        
    canada_avg=get_region_avg('Canada')
    cali_avg=get_region_avg('California')
    gom_avg=get_region_avg('Gulf of Mexico')

    return render_template('/initial_routes/square10.html', canada_avg=canada_avg, cali_avg=cali_avg, gom_avg=gom_avg)

@routes.route("/region/11", methods=["GET"])
def region11_page():
    if not g.user:
        return redirect("/home")
        
    cali_avg=get_region_avg('California')
    natlantic_avg=get_region_avg('US East Coast (N. Atlantic Ocean)')
    greenland_avg=get_region_avg('Greenland')

    return render_template('/initial_routes/square11.html', cali_avg=cali_avg, natlantic_avg=natlantic_avg, greenland_avg=greenland_avg)

@routes.route("/region/12", methods=["GET"])
def region12_page():
    if not g.user:
        return redirect("/home")
        
    nsea_avg=get_region_avg('North Sea')
    nwafrica_avg=get_region_avg('NW Africa / Morocco')

    return render_template('/initial_routes/square12.html', nsea_avg=nsea_avg, nwafrica_avg=nwafrica_avg)

@routes.route("/region/13", methods=["GET"])
def region13_page():
    if not g.user:
        return redirect("/home")
        
    nsea_avg=get_region_avg('North Sea')
    medsea_avg=get_region_avg('Mediterranean Sea')
    blacksea_avg=get_region_avg('Black Sea')
    caspsea_avg=get_region_avg('Caspian Sea')
    persia_avg=get_region_avg('Persian Gulf')

    return render_template('/initial_routes/square13.html', nsea_avg=nsea_avg, medsea_avg=medsea_avg, blacksea_avg=blacksea_avg, caspsea_avg=caspsea_avg, persia_avg=persia_avg)

@routes.route("/region/14", methods=["GET"])
def region14_page():
    """no entry page - reroute home or disable click"""
    if not g.user:
        return redirect("/home")
        
    return redirect("/home")

@routes.route("/region/15", methods=["GET"])
def region15_page():
    if not g.user:
        return redirect("/home")
        
    skorea_avg=get_region_avg('S. Korea / Japan')
    china_avg=get_region_avg('China / Vietnam')
    russia_avg=get_region_avg('Russia')

    return render_template('/initial_routes/square15.html', skorea_avg=skorea_avg, china_avg=china_avg, russia_avg=russia_avg)

@routes.route("/region/16", methods=["GET"])
def region16_page():
    if not g.user:
        return redirect("/home")
        
    skorea_avg=get_region_avg('S. Korea / Japan')
    china_avg=get_region_avg('China / Vietnam')
    russia_avg=get_region_avg('Russia')

    return render_template('/initial_routes/square16.html', skorea_avg=skorea_avg, china_avg=china_avg, russia_avg=russia_avg)
    
@routes.route("/region/17", methods=["GET"])
def region17_page():
    if not g.user:
        return redirect("/home")
                
    hawaii_avg=get_region_avg('Hawaii')

    return redirect("/hawaii")

@routes.route("/region/18", methods=["GET"])
def region18_page():
    if not g.user:
        return redirect("/home")
        
    mexico_avg=get_region_avg('Mexico (Pacific)')
    gom_avg=get_region_avg('Gulf of Mexico')
    columbia_avg=get_region_avg('Columbia')
    equador_avg=get_region_avg('Equador')
    peru_avg=get_region_avg('Peru')


    return render_template('/initial_routes/square18.html', mexico_avg=mexico_avg, gom_avg=gom_avg, columbia_avg=columbia_avg, equador_avg=equador_avg, peru_avg=peru_avg)

@routes.route("/region/19", methods=["GET"])
def region19_page():
    if not g.user:
        return redirect("/home")
        
    gom_avg=get_region_avg('Gulf of Mexico')
    caribbean_avg=get_region_avg('Caribbean')
    guyana_avg=get_region_avg('Guyana')
    suriname_avg=get_region_avg('Suriname')
    fguiana_avg=get_region_avg('French Guiana')

    return render_template('/initial_routes/square19.html', gom_avg=gom_avg, caribbean_avg=caribbean_avg, guyana_avg=guyana_avg, suriname_avg=suriname_avg, fguiana_avg=fguiana_avg)

@routes.route("/region/20", methods=["GET"])
def region20_page():
    if not g.user:
        return redirect("/home")
        
    ghana_avg=get_region_avg('Ghana')
    nigeria_avg=get_region_avg('Nigeria')
    gabon_avg=get_region_avg('Gabon')
    angola_avg=get_region_avg('Angola')
    ethiopia_avg=get_region_avg('Ethiopia')

    return render_template('/initial_routes/square20.html', ghana_avg=ghana_avg, nigeria_avg=nigeria_avg, gabon_avg=gabon_avg, angola_avg=angola_avg, ethiopia_avg=ethiopia_avg)

@routes.route("/region/21", methods=["GET"])
def region21_page():
    if not g.user:
        return redirect("/home")
        
    ghana_avg=get_region_avg('Ghana')
    nigeria_avg=get_region_avg('Nigeria')
    gabon_avg=get_region_avg('Gabon')
    sierraleone_avg=get_region_avg('Sierra Leone')
    mauritania_avg=get_region_avg('Mauritania')

    return render_template('/initial_routes/square21.html', ghana_avg=ghana_avg, nigeria_avg=nigeria_avg, gabon_avg=gabon_avg, sierraleone_avg=sierraleone_avg, mauritania_avg=mauritania_avg)

@routes.route("/region/22", methods=["GET"])
def region22_page():
    if not g.user:
        return redirect("/home")
        
    india_avg=get_region_avg('India / Sri Lanka')
    malaysia_avg=get_region_avg('Malaysia')
    indonesia_avg=get_region_avg('Indonesia')

    return render_template('/initial_routes/square22.html', malaysia_avg=malaysia_avg, indonesia_avg=indonesia_avg, india_avg=india_avg)

@routes.route("/region/23", methods=["GET"])
def region23_page():
    if not g.user:
        return redirect("/home")
        
    phil_avg=get_region_avg('Ghana')
    malaysia_avg=get_region_avg('Malaysia')
    indonesia_avg=get_region_avg('Indonesia')
    schina_avg=get_region_avg('Southern China')
    ausnz_avg=get_region_avg('Australia / New Zealand')

    return render_template('/initial_routes/square23.html', phil_avg=phil_avg, malaysia_avg=malaysia_avg, indonesia_avg=indonesia_avg, schina_avg=schina_avg, ausnz_avg=ausnz_avg)

@routes.route("/region/24", methods=["GET"])
def region24_page():
    """single entry page - reroute to country"""
    if not g.user:
        return redirect("/home")
        
    return redirect('/australia_newzealand')

@routes.route("/region/25", methods=["GET"])
def region25_page():
    """no entry page - reroute home or disable click"""
    if not g.user:
        return redirect("/home")
        
    return redirect("/home")

@routes.route("/region/26", methods=["GET"])
def region26_page():
    if not g.user:
        return redirect("/home")
        
    chile_avg=get_region_avg('Chile')
    argentina_avg=get_region_avg('Argentina')

    return render_template('/initial_routes/square26.html', chile_avg=chile_avg, argentina_avg=argentina_avg)

@routes.route("/region/27", methods=["GET"])
def region27_page():
    if not g.user:
        return redirect("/home")
        
    brazil_avg=get_region_avg('Brazil')
    uruguay_avg=get_region_avg('Uruguay')
    antartica_avg=get_region_avg('Antarctica')
    chile_avg=get_region_avg('Chile')
    argentina_avg=get_region_avg('Argentina')
    falkland_avg=get_region_avg('Falkland Islands')


    return render_template('/initial_routes/square27.html', brazil_avg=brazil_avg, uruguay_avg=uruguay_avg, antartica_avg=antartica_avg, chile_avg=chile_avg, argentina_avg=argentina_avg, falkland_avg=falkland_avg)

@routes.route("/region/28", methods=["GET"])
def region28_page():
    if not g.user:
        return redirect("/home")
        
    brazil_avg=get_region_avg('Brazil')
    uruguay_avg=get_region_avg('Uruguay')
    antartica_avg=get_region_avg('Antarctica')
    angola_avg=get_region_avg('Angola')
    namibia_avg=get_region_avg('Namibia')
    safrica_avg=get_region_avg('South Africa')

    return render_template('/initial_routes/square28.html', brazil_avg=brazil_avg, uruguay_avg=uruguay_avg, antartica_avg=antartica_avg, angola_avg=angola_avg, namibia_avg=namibia_avg, safrica_avg=safrica_avg)

@routes.route("/region/29", methods=["GET"])
def region29_page():
    if not g.user:
        return redirect("/home")
        
    angola_avg=get_region_avg('Angola')
    namibia_avg=get_region_avg('Namibia')
    mozambique_avg=get_region_avg('Mozambique')
    madagascar_avg=get_region_avg('Madagascar')

    return render_template('/initial_routes/square29.html')

@routes.route("/region/30", methods=["GET"])
def region30_page():
    """no entry page - reroute home or disable click"""
    if not g.user:
        return redirect("/home")
        
    return redirect("/home")

@routes.route("/region/31", methods=["GET"])
def region31_page():
    """single entry page - reroute to country"""
    if not g.user:
        return redirect("/home")
        
    return redirect('/australia_newzealand')

@routes.route("/region/32", methods=["GET"])
def region32_page():
    """single entry page - reroute to country"""
    if not g.user:
        return redirect("/home")
        
    return redirect('/australia_newzealand')
