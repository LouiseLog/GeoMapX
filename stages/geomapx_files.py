

import os
import shutil

def copy_geomapx_files(args):
    """
    Rename files in the project directory
    """
    # Rename the files

    
    path_dem = os.path.join(args.project_path, "odm_dem")
    path_ortho = os.path.join(args.project_path, "odm_orthophoto")
    path_report = os.path.join(args.project_path, "odm_report")
    path_texturing = os.path.join(args.project_path, "odm_texturing")
    path_georef = os.path.join(args.project_path, "odm_georeferencing")

    path_geomapx = os.path.join(args.project_path, "output", "geomapx")

    path_geomapx_mdem = os.path.join(path_geomapx, "Modelos_Digitais_de_Elevação")
    path_geomapx_ortho = os.path.join(path_geomapx, "Ortophotos")
    path_geomapx_report = os.path.join(path_geomapx, "Relatórios_GeoMapX")
    path_geomapx_texturing = os.path.join(path_geomapx, "Texturizações")
    path_geomapx_georef = os.path.join(path_geomapx, "Georreferenciamentos")

    path_dem_dsm = os.path.join(path_dem, "dsm.tif")
    path_dem_dtm = os.path.join(path_dem, "dtm.tif")
    path_ortho_kmz = os.path.join(path_ortho, "odm_orthophoto.kmz")
    path_ortho_png = os.path.join(path_ortho, "odm_orthophoto.png")
    path_ortho_tif = os.path.join(path_ortho, "odm_orthophoto.tif")
    path_report_pdf = os.path.join(path_report, "report.pdf")
    path_texturing_model_obj = os.path.join(path_texturing, "odm_textured_model_geo.obj")
    path_georef_model_csv = os.path.join(path_georef, "odm_georeferenced_model.csv")
    path_georef_model_laz = os.path.join(path_georef, "odm_georeferenced_model.laz")

    path_geomapx_mdem_dsm = os.path.join(path_geomapx_mdem, "Modelo_Digital_de_Superfície.tif")
    path_geomapx_mdem_dtm = os.path.join(path_geomapx_mdem, "Modelo_Digital_de_Terreno.tif")
    path_geomapx_ortho_kmz = os.path.join(path_geomapx_ortho, "Ortofoto.kmz")
    path_geomapx_ortho_png = os.path.join(path_geomapx_ortho, "Ortofoto.png")
    path_geomapx_ortho_tif = os.path.join(path_geomapx_ortho, "Ortofoto.tif")
    path_geomapx_report_pdf = os.path.join(path_geomapx_report, "Relatório.pdf")
    path_geomapx_texturing_model_obj = os.path.join(path_geomapx_texturing, "Modelo_Texturizado.obj")
    path_geomapx_georef_model_csv = os.path.join(path_geomapx_georef, "Nuvem_de_Pontos.csv")
    path_geomapx_georef_model_laz = os.path.join(path_geomapx_georef, "Nuvem_de_Pontos.laz")

    path_geomapx_zip = os.path.join(args.project_path, "arquivos_geomapx")

    os.mkdir(path_geomapx)
    os.mkdir(path_geomapx_mdem)
    os.mkdir(path_geomapx_ortho)
    os.mkdir(path_geomapx_report)
    os.mkdir(path_geomapx_texturing)
    os.mkdir(path_geomapx_georef)
    shutil.copy(path_dem_dsm, path_geomapx_mdem_dsm)
    shutil.copy(path_dem_dtm, path_geomapx_mdem_dtm)
    shutil.copy(path_ortho_kmz, path_geomapx_ortho_kmz)
    shutil.copy(path_ortho_png, path_geomapx_ortho_png)
    shutil.copy(path_ortho_tif, path_geomapx_ortho_tif)
    shutil.copy(path_report_pdf, path_geomapx_report_pdf)
    shutil.copy(path_texturing_model_obj, path_geomapx_texturing_model_obj)
    shutil.copy(path_georef_model_csv, path_geomapx_georef_model_csv)
    shutil.copy(path_georef_model_laz, path_geomapx_georef_model_laz)
    shutil.make_archive(path_geomapx, 'zip', path_geomapx_zip)


    """
    shutil.copytree(path_dem, path_geomapx_mdem)
    shutil.copytree(path_ortho, path_geomapx_ortho)
    shutil.copytree(path_report, path_geomapx_report)
    shutil.copytree(path_texturing, path_geomapx_texturing)
    shutil.copytree(path_georef, path_geomapx_georef)
    """

    """
    for root, dirs, files in os.walk(args.project_path):
        for file in files:
            if file.endswith(".json"):
                new_name = file.replace(".json", ".jsonl")
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
    """



    #os.mkdir(os.path.join(args.project_path, "geomapx", "Visualização_3D"))
