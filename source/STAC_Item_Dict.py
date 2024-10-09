{'type': 'Feature', 
 'stac_version': '1.0.0', 
 'id': 'S2A_17TQM_20190731_0_L2A', 
 'properties': {
'created': '2022-11-08T09:27:10.244Z', 
'platform': 'sentinel-2a', 
'constellation': 'sentinel-2', 
'instruments': ['msi'], 
'eo:cloud_cover': 0.598804, 
'proj:epsg': 32617, 
'mgrs:utm_zone': 17, 
'mgrs:latitude_band': 'T', 
'mgrs:grid_square': 'QM', 
'grid:code': 'MGRS-17TQM', 
'view:sun_azimuth': 152.775522686856, 
'view:sun_elevation': 59.478197741673995, 
's2:degraded_msi_data_percentage': 0, 
's2:nodata_pixel_percentage': 4.3e-05, 
's2:saturated_defective_pixel_percentage': 0, 
's2:dark_features_percentage': 0.887765, 
's2:cloud_shadow_percentage': 0.144615, 
's2:vegetation_percentage': 90.678644, 
's2:not_vegetated_percentage': 0.415214, 
's2:water_percentage': 6.981274, 
's2:unclassified_percentage': 0.293679, 
's2:medium_proba_clouds_percentage': 0.228855, 
's2:high_proba_clouds_percentage': 0.116154, 
's2:thin_cirrus_percentage': 0.253795, 
's2:snow_ice_percentage': 0, 
's2:product_type': 'S2MSI2A', 
's2:processing_baseline': '02.13', 
's2:product_uri': 'S2A_MSIL2A_20190731T160911_N0213_R140_T17TQM_20190731T223121.SAFE', 
's2:generation_time': '2019-07-31T22:31:21.000000Z', 
's2:datatake_id': 'GS2A_20190731T160911_021444_N02.13', 
's2:datatake_type': 'INS-NOBS', 
's2:datastrip_id': 'S2A_OPER_MSI_L2A_DS_MTI__20190731T223121_S20190731T161908_N02.13', 
's2:granule_id': 'S2A_OPER_MSI_L2A_TL_MTI__20190731T223121_A021444_T17TQM_N02.13', 
's2:reflectance_conversion_factor': 0.969766011178338, 
'datetime': '2019-07-31T16:20:29.760000Z', 
's2:sequence': '0', 
'earthsearch:s3_path': 's3://sentinel-cogs/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A', 
'earthsearch:payload_id': 'roda-sentinel2/workflow-sentinel2-to-stac/7ff82b28de72997bf6e6086749b7915f', 
'earthsearch:boa_offset_applied': False, 
'processing:software': {'sentinel2-to-stac': '0.1.0'}, 
'updated': '2022-11-08T09:27:10.244Z'}, 
 'geometry': {'type': 'Polygon', 'coordinates': [[[-78.37350196345521, 46.92356376720102], [-76.93435663785229, 46.881451150611014], [-77.00701004782671, 45.895744680146535], [-78.42052724063872, 45.93643957284447], [-78.37350196345521, 46.92356376720102]]]}, 
 'links': [{'rel': 'self', 'href': 'https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_17TQM_20190731_0_L2A', 
           'type': 'application/geo+json'}, 
           {'rel': 'canonical', 'href': 's3://sentinel-cogs/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/S2A_17TQM_20190731_0_L2A.json', 'type': 'application/json'}, 
           {'rel': 'license', 'href': 'https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice'}, 
           {'rel': 'derived_from', 'href': 'https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items/S2A_17TQM_20190731_0_L1C', 'type': 'application/geo+json'}, 
           {'rel': 'parent', 'href': 'https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a', 'type': 'application/json'}, 
           {'rel': 'collection', 'href': 'https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a', 'type': 'application/json'}, 
           {'rel': 'root', 'href': 'https://earth-search.aws.element84.com/v1', 'type': 'application/json', 'title': 'Earth Search by Element 84'}, 
           {'rel': 'thumbnail', 'href': 'https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_17TQM_20190731_0_L2A/thumbnail'}], 

'assets': {'aot': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/AOT.tif', 
                   'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                   'title': 'Aerosol optical thickness (AOT)', 
                   'proj:shape': [5490, 5490], 
                   'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                   'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.001, 'offset': 0}], 
                   'roles': ['data', 'reflectance']
                  }, 
           'blue': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B02.tif', 
                    'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                    'title': 'Blue (band 2) - 10m', 
                    'eo:bands': [{'name': 'blue', 'common_name': 'blue', 'description': 'Blue (band 2)', 'center_wavelength': 0.49, 'full_width_half_max': 0.098}], 
                    'gsd': 10, 
                    'proj:shape': [10980, 10980], 
                    'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                    'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                    'roles': ['data', 'reflectance']
                   }, 

           'coastal': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B01.tif', 
                       'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                       'title': 'Coastal aerosol (band 1) - 60m', 
                       'eo:bands': [{'name': 'coastal', 'common_name': 'coastal', 'description': 'Coastal aerosol (band 1)', 'center_wavelength': 0.443, 'full_width_half_max': 0.027}], 
                       'gsd': 60, 
                       'proj:shape': [1830, 1830], 
                       'proj:transform': [60, 0, 699960, 0, -60, 5200020], 
                       'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 60, 'scale': 0.0001, 'offset': 0}], 
                       'roles': ['data', 'reflectance']
                      }, 
           'granule_metadata': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/granule_metadata.xml', 
                                'type': 'application/xml', 
                                'roles': ['metadata']}, 
           'green': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B03.tif', 
                     'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                     'title': 'Green (band 3) - 10m', 
                     'eo:bands': [{'name': 'green', 'common_name': 'green', 'description': 'Green (band 3)', 'center_wavelength': 0.56, 'full_width_half_max': 0.045}], 
                     'gsd': 10, 
                     'proj:shape': [10980, 10980], 
                     'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                     'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                     'roles': ['data', 'reflectance']
                    }, 
           'nir': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B08.tif', 
                   'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                   'title': 'NIR 1 (band 8) - 10m', 
                   'eo:bands': [{'name': 'nir', 'common_name': 'nir', 'description': 'NIR 1 (band 8)', 'center_wavelength': 0.842, 'full_width_half_max': 0.145}], 
                   'gsd': 10, 
                   'proj:shape': [10980, 10980], 
                   'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                   'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                   'roles': ['data', 'reflectance']
                  }, 
           'nir08': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B8A.tif', 
                     'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                     'title': 'NIR 2 (band 8A) - 20m', 
                     'eo:bands': [{'name': 'nir08', 'common_name': 'nir08', 'description': 'NIR 2 (band 8A)', 'center_wavelength': 0.865, 'full_width_half_max': 0.033}], 
                     'gsd': 20, 
                     'proj:shape': [5490, 5490], 
                     'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                     'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                     'roles': ['data', 'reflectance']
                    }, 
           'nir09': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B09.tif', 
                     'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                     'title': 'NIR 3 (band 9) - 60m', 
                     'eo:bands': [{'name': 'nir09', 'common_name': 'nir09', 'description': 'NIR 3 (band 9)', 'center_wavelength': 0.945, 'full_width_half_max': 0.026}], 
                     'gsd': 60, 
                     'proj:shape': [1830, 1830], 
                     'proj:transform': [60, 0, 699960, 0, -60, 5200020], 
                     'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 60, 'scale': 0.0001, 'offset': 0}], 
                     'roles': ['data', 'reflectance']
                    },
           'red': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B04.tif', 
                   'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                   'title': 'Red (band 4) - 10m', 
                   'eo:bands': [{'name': 'red', 'common_name': 'red', 'description': 'Red (band 4)', 'center_wavelength': 0.665, 'full_width_half_max': 0.038}], 
                   'gsd': 10, 
                   'proj:shape': [10980, 10980], 
                   'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                   'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                   'roles': ['data', 'reflectance']
                  }, 
           'rededge1': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B05.tif', 
                        'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                        'title': 'Red edge 1 (band 5) - 20m', 
                        'eo:bands': [{'name': 'rededge1', 'common_name': 'rededge', 'description': 'Red edge 1 (band 5)', 'center_wavelength': 0.704, 'full_width_half_max': 0.019}], 
                        'gsd': 20, 
                        'proj:shape': [5490, 5490], 
                        'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                       }, 
           'rededge2': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B06.tif', 
                        'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                        'title': 'Red edge 2 (band 6) - 20m', 
                        'eo:bands': [{'name': 'rededge2', 'common_name': 'rededge', 'description': 'Red edge 2 (band 6)', 'center_wavelength': 0.74, 'full_width_half_max': 0.018}], 
                        'gsd': 20, 
                        'proj:shape': [5490, 5490], 
                        'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                       }, 
           'rededge3': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B07.tif', 
                        'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                        'title': 'Red edge 3 (band 7) - 20m', 
                        'eo:bands': [{'name': 'rededge3', 'common_name': 'rededge', 'description': 'Red edge 3 (band 7)', 'center_wavelength': 0.783, 'full_width_half_max': 0.028}], 
                        'gsd': 20, 
                        'proj:shape': [5490, 5490], 
                        'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                        }, 
           'scl': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/SCL.tif', 
                   'type': 'image/tiff; application=geotiff; profile=cloud-optimized',
                   'title': 'Scene classification map (SCL)',
                   'proj:shape': [5490, 5490], 
                   'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                   'raster:bands': [{'nodata': 0, 'data_type': 'uint8', 'spatial_resolution': 20}], 
                   'roles': ['data', 'reflectance']
                  },                    
           'swir16': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B11.tif', 
                      'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                      'title': 'SWIR 1 (band 11) - 20m', 
                      'eo:bands': [{'name': 'swir16', 'common_name': 'swir16', 'description': 'SWIR 1 (band 11)', 'center_wavelength': 1.61, 'full_width_half_max': 0.143}], 
                      'gsd': 20, 
                      'proj:shape': [5490, 5490], 
                      'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                      'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                      'roles': ['data', 'reflectance']
                     }, 
           'swir22': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/B12.tif', 
                      'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                      'title': 'SWIR 2 (band 12) - 20m', 
                      'eo:bands': [{'name': 'swir22', 'common_name': 'swir22', 'description': 'SWIR 2 (band 12)', 'center_wavelength': 2.19, 'full_width_half_max': 0.242}], 
                      'gsd': 20, 
                      'proj:shape': [5490, 5490], 
                      'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                      'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                      'roles': ['data', 'reflectance']
                     }, 
           'thumbnail': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/thumbnail.jpg', 
                         'type': 'image/jpeg', 
                         'title': 'Thumbnail image', 
                         'roles': ['thumbnail']
                        }, 
           'tileinfo_metadata': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/tileinfo_metadata.json', 
                                 'type': 'application/json', 
                                 'roles': ['metadata']
                                }, 
           'visual': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/TCI.tif', 
                      'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                      'title': 'True color image', 
                      'eo:bands': [{'name': 'red', 'common_name': 'red', 'description': 'Red (band 4)', 'center_wavelength': 0.665, 'full_width_half_max': 0.038}, 
                                   {'name': 'green', 'common_name': 'green', 'description': 'Green (band 3)', 'center_wavelength': 0.56, 'full_width_half_max': 0.045}, 
                                   {'name': 'blue', 'common_name': 'blue', 'description': 'Blue (band 2)', 'center_wavelength': 0.49, 'full_width_half_max': 0.098}], 
                      'proj:shape': [10980, 10980], 
                      'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                      'roles': ['visual']
                     }, 
           'wvp': {'href': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/17/T/QM/2019/7/S2A_17TQM_20190731_0_L2A/WVP.tif', 
                   'type': 'image/tiff; application=geotiff; profile=cloud-optimized', 
                   'title': 'Water vapour (WVP)', 
                   'proj:shape': [5490, 5490], 
                   'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                   'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'unit': 'cm', 'scale': 0.001, 'offset': 0}], 
                   'roles': ['data', 'reflectance']
                   }, 
           'aot-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/AOT.jp2', 
                       'type': 'image/jp2', 
                       'title': 'Aerosol optical thickness (AOT)', 
                       'proj:shape': [5490, 5490], 
                       'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                       'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.001, 'offset': 0}], 
                       'roles': ['data', 'reflectance']
                       }, 
           'blue-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B02.jp2', 
                        'type': 'image/jp2', 
                        'title': 'Blue (band 2) - 10m', 
                        'eo:bands': [{'name': 'blue', 'common_name': 'blue', 'description': 'Blue (band 2)', 'center_wavelength': 0.49, 'full_width_half_max': 0.098}], 
                        'gsd': 10, 
                        'proj:shape': [10980, 10980], 
                        'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                        }, 
            'coastal-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B01.jp2', 
                            'type': 'image/jp2', 
                            'title': 'Coastal aerosol (band 1) - 60m', 
                            'eo:bands': [{'name': 'coastal', 'common_name': 'coastal', 'description': 'Coastal aerosol (band 1)', 'center_wavelength': 0.443, 'full_width_half_max': 0.027}], 
                            'gsd': 60, 
                            'proj:shape': [1830, 1830], 
                            'proj:transform': [60, 0, 699960, 0, -60, 5200020], 
                            'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 60, 'scale': 0.0001, 'offset': 0}], 
                            'roles': ['data', 'reflectance']
                            }, 
            'green-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B03.jp2', 
                          'type': 'image/jp2', 
                          'title': 'Green (band 3) - 10m', 
                          'eo:bands': [{'name': 'green', 'common_name': 'green', 'description': 'Green (band 3)', 'center_wavelength': 0.56, 'full_width_half_max': 0.045}], 
                          'gsd': 10, 
                          'proj:shape': [10980, 10980], 
                          'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                          'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                          'roles': ['data', 'reflectance']
                          }, 
            'nir-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B08.jp2', 
                        'type': 'image/jp2', 'title': 'NIR 1 (band 8) - 10m', 
                        'eo:bands': [{'name': 'nir', 'common_name': 'nir', 'description': 'NIR 1 (band 8)', 'center_wavelength': 0.842, 'full_width_half_max': 0.145}], 
                        'gsd': 10, 
                        'proj:shape': [10980, 10980], 
                        'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                        }, 
            'nir08-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B8A.jp2', 
                          'type': 'image/jp2', 
                          'title': 'NIR 2 (band 8A) - 20m', 
                          'eo:bands': [{'name': 'nir08', 'common_name': 'nir08', 'description': 'NIR 2 (band 8A)', 'center_wavelength': 0.865, 'full_width_half_max': 0.033}], 
                          'gsd': 20, 
                          'proj:shape': [5490, 5490], 
                          'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                          'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                          'roles': ['data', 'reflectance']
                          }, 
            'nir09-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B09.jp2', 
                          'type': 'image/jp2', 
                          'title': 'NIR 3 (band 9) - 60m', 
                          'eo:bands': [{'name': 'nir09', 'common_name': 'nir09', 'description': 'NIR 3 (band 9)', 'center_wavelength': 0.945, 'full_width_half_max': 0.026}], 
                          'gsd': 60, 
                          'proj:shape': [1830, 1830], 
                          'proj:transform': [60, 0, 699960, 0, -60, 5200020], 
                          'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 60, 'scale': 0.0001, 'offset': 0}], 
                          'roles': ['data', 'reflectance']
                          }, 
            'red-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B04.jp2', 
                        'type': 'image/jp2', 
                        'title': 'Red (band 4) - 10m', 
                        'eo:bands': [{'name': 'red', 'common_name': 'red', 'description': 'Red (band 4)', 'center_wavelength': 0.665, 'full_width_half_max': 0.038}], 
                        'gsd': 10, 
                        'proj:shape': [10980, 10980], 
                        'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 10, 'scale': 0.0001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']
                        }, 
            'rededge1-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B05.jp2', 
                             'type': 'image/jp2', 
                             'title': 'Red edge 1 (band 5) - 20m', 
                             'eo:bands': [{'name': 'rededge1', 'common_name': 'rededge', 'description': 'Red edge 1 (band 5)', 'center_wavelength': 0.704, 'full_width_half_max': 0.019}], 
                             'gsd': 20, 
                             'proj:shape': [5490, 5490], 
                             'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                             'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                             'roles': ['data', 'reflectance']
                             },
            'rededge2-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B06.jp2', 
                             'type': 'image/jp2', 
                             'title': 'Red edge 2 (band 6) - 20m', 
                             'eo:bands': [{'name': 'rededge2', 'common_name': 'rededge', 'description': 'Red edge 2 (band 6)', 'center_wavelength': 0.74, 'full_width_half_max': 0.018}], 
                             'gsd': 20, 
                             'proj:shape': [5490, 5490], 
                             'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                             'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                             'roles': ['data', 'reflectance']}, 
            'rededge3-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B07.jp2', 
                             'type': 'image/jp2', 
                             'title': 'Red edge 3 (band 7) - 20m', 
                             'eo:bands': [{'name': 'rededge3', 'common_name': 'rededge', 'description': 'Red edge 3 (band 7)', 'center_wavelength': 0.783, 'full_width_half_max': 0.028}], 
                             'gsd': 20, 
                             'proj:shape': [5490, 5490], 
                             'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                             'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                             'roles': ['data', 'reflectance']
                             }, 
            'scl-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/SCL.jp2', 
                        'type': 'image/jp2', 
                        'title': 'Scene classification map (SCL)', 
                        'proj:shape': [5490, 5490], 
                        'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint8', 'spatial_resolution': 20}], 
                        'roles': ['data', 'reflectance']
                        }, 
            'swir16-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B11.jp2', 
                           'type': 'image/jp2', 
                           'title': 'SWIR 1 (band 11) - 20m', 
                           'eo:bands': [{'name': 'swir16', 'common_name': 'swir16', 'description': 'SWIR 1 (band 11)', 'center_wavelength': 1.61, 'full_width_half_max': 0.143}], 
                           'gsd': 20, 
                           'proj:shape': [5490, 5490], 
                           'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                           'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                           'roles': ['data', 'reflectance']
                           }, 
            'swir22-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/B12.jp2', 
                           'type': 'image/jp2', 
                           'title': 'SWIR 2 (band 12) - 20m', 
                           'eo:bands': [{'name': 'swir22', 'common_name': 'swir22', 'description': 'SWIR 2 (band 12)', 'center_wavelength': 2.19, 'full_width_half_max': 0.242}], 
                           'gsd': 20, 
                           'proj:shape': [5490, 5490], 
                           'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                           'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'scale': 0.0001, 'offset': 0}], 
                           'roles': ['data', 'reflectance']
                           }, 
            'visual-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/TCI.jp2', 
                           'type': 'image/jp2', 
                           'title': 'True color image', 
                           'eo:bands': [{'name': 'red', 'common_name': 'red', 'description': 'Red (band 4)', 'center_wavelength': 0.665, 'full_width_half_max': 0.038}, 
                                        {'name': 'green', 'common_name': 'green', 'description': 'Green (band 3)', 'center_wavelength': 0.56, 'full_width_half_max': 0.045}, 
                                        {'name': 'blue', 'common_name': 'blue', 'description': 'Blue (band 2)', 'center_wavelength': 0.49, 'full_width_half_max': 0.098}], 
                           'proj:shape': [10980, 10980], 
                           'proj:transform': [10, 0, 699960, 0, -10, 5200020], 
                           'roles': ['visual']
                           }, 
            'wvp-jp2': {'href': 's3://sentinel-s2-l2a/tiles/17/T/QM/2019/7/31/0/WVP.jp2', 
                        'type': 'image/jp2', 
                        'title': 'Water vapour (WVP)', 
                        'proj:shape': [5490, 5490], 
                        'proj:transform': [20, 0, 699960, 0, -20, 5200020], 
                        'raster:bands': [{'nodata': 0, 'data_type': 'uint16', 'bits_per_sample': 15, 'spatial_resolution': 20, 'unit': 'cm', 'scale': 0.001, 'offset': 0}], 
                        'roles': ['data', 'reflectance']}}, 
            'bbox': [-78.42052724063872, 45.895744680146535, -76.93435663785229, 46.92356376720102], 
            'stac_extensions': ['https://stac-extensions.github.io/grid/v1.0.0/schema.json', 
                                'https://stac-extensions.github.io/view/v1.0.0/schema.json', 
                                'https://stac-extensions.github.io/processing/v1.1.0/schema.json', 
                                'https://stac-extensions.github.io/eo/v1.0.0/schema.json', 
                                'https://stac-extensions.github.io/projection/v1.0.0/schema.json', 
                                'https://stac-extensions.github.io/mgrs/v1.0.0/schema.json', 
                                'https://stac-extensions.github.io/raster/v1.1.0/schema.json'], 
            'collection': 'sentinel-2-l2a'}