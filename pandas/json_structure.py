
data = {
  "issues": {
    "CHECKIN": {
      "issue_name": "Checkin",
      "issue_key": "CHECKIN",
      "done": 'false',
      "store_status": [
        "SUCCESS",
        "UNSUCCESS"
      ],
      "validate": {
        "required": 'true'
      },
      "value": {
        "lat": 'null',
        "lng": 'null'
      }
    },
    "CAMERA": {
      "issue_name": "Camera",
      "issue_key": "CAMERA",
      "done": 'false',
      "store_status": [
        "SUCCESS",
        "UNSUCCESS"
      ],
      "validate": {
        "required": 'true'
      },
      "items": [
        {
          "type_id": 111,
          "type_name": "Chụp hình tổng quan cửa hàng",
          "store_status": [
            "SUCCESS",
            "UNSUCCESS"
          ],
          "validate": {
            "required": 'true',
            "min": 1,
            "max": 15
          },
          "value": []
        },
        {
          "type_id": 112,
          "type_name": "Chụp selfie",
          "store_status": [
            "SUCCESS",
            "UNSUCCESS"
          ],
          "validate": {
            "required": 'true',
            "min": 1,
            "max": 15
          },
          "value": []
        },
        {
            "type_id": 115,
            "type_name": "Setup CH mới - TRƯỚC khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          },
          {
            "type_id": 116,
            "type_name": "Setup CH mới - SAU khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          },
          {
            "type_id": 117,
            "type_name": "Lắp đặt POSM - TRƯỚC khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          },
          {
            "type_id": 118,
            "type_name": "Lắp đặt POSM - SAU khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          },
          {
            "type_id": 119,
            "type_name": "Win vị trí - TRƯỚC khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          },
          {
            "type_id": 120,
            "type_name": "Win vị trí - SAU khi làm",
            "store_status": [
              "SUCCESS"
            ],
            "validate": {
              "required": 'true',
              "min": 1,
              "max": 15
            },
            "value": []
          }
      ]
    },
    "FACING": {
      "issue_name": "Facing",
      "issue_key": "FACING",
      "done": 'false',
      "store_status": [
        "SUCCESS"
      ],
      "validate": {
        "required": 'true'
      },
      "items": [
        {
          "planogram_id": "PLG_STORE_001",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "FGSUPERL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (Super & L)",
              "skus": [
                {
                  "sku_code": "CMDSTORE0003",
                  "sku_name": "Setup HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0007",
                  "sku_name": "Setup PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0006",
                  "sku_name": "Setup Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0005",
                  "sku_name": "Setup Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0002",
                  "sku_name": "Setup GE",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup Sachet",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0009",
                  "sku_name": "Setup Ụ đảo",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_002",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "FGSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (S & XS)",
              "skus": [
                {
                  "sku_code": "CMDSTORE0003",
                  "sku_name": "Setup HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0007",
                  "sku_name": "Setup PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0006",
                  "sku_name": "Setup Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0005",
                  "sku_name": "Setup Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0002",
                  "sku_name": "Setup GE",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_003",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "HBL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B L",
              "skus": [
                {
                  "sku_code": "CMDSTORE0004",
                  "sku_name": "Setup Kệ chính",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_004",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "HBM"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B M",
              "skus": [
                {
                  "sku_code": "CMDSTORE0004",
                  "sku_name": "Setup Kệ chính",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_005",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "HBSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B S & XS",
              "skus": [
                {
                  "sku_code": "CMDSTORE0004",
                  "sku_name": "Setup Kệ chính",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_006",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "MP"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P",
              "skus": [
                {
                  "sku_code": "CMDSTORE0004",
                  "sku_name": "Setup Kệ chính",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_007",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "MXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P XS",
              "skus": [
                {
                  "sku_code": "CMDSTORE0004",
                  "sku_name": "Setup Kệ chính",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDSTORE0008",
                  "sku_name": "Setup Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_STORE_008",
          "planogram_name": "Setup CH mới",
          "image_type_id": ["115","116"],
          "region": [],
          "store_types": [
            "MS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "MS",
              "skus": [
                {
                  "sku_code": "CMDSTORE0001",
                  "sku_name": "Setup Full store",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_001",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "FGSUPERL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (Super & L)",
              "skus": [
                {
                  "sku_code": "CMDPOSM0022",
                  "sku_name": "Window Frame-POSM PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0019",
                  "sku_name": "Window Frame-POSM HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0021",
                  "sku_name": "Window Frame-POSM Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0020",
                  "sku_name": "Window Frame-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0009",
                  "sku_name": "PET-POSM Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0008",
                  "sku_name": "PET-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0007",
                  "sku_name": "PET-POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0006",
                  "sku_name": "PET-POSM Khung HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0001",
                  "sku_name": "GE/FSU-POSM GE/FSU",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_002",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "FGSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (S & XS)",
              "skus": [
                {
                  "sku_code": "CMDPOSM0022",
                  "sku_name": "Window Frame-POSM PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0019",
                  "sku_name": "Window Frame-POSM HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0021",
                  "sku_name": "Window Frame-POSM Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0020",
                  "sku_name": "Window Frame-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0009",
                  "sku_name": "PET-POSM Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0008",
                  "sku_name": "PET-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0007",
                  "sku_name": "PET-POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0006",
                  "sku_name": "PET-POSM Khung HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0001",
                  "sku_name": "GE/FSU-POSM GE/FSU",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_003",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "HBL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B L",
              "skus": [
                {
                  "sku_code": "CMDPOSM0018",
                  "sku_name": "Window Frame -POSM Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0017",
                  "sku_name": "Window Frame -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0016",
                  "sku_name": "Window Frame -POSM Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0015",
                  "sku_name": "Window Frame -POSM Khung Men",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0005",
                  "sku_name": "PET -POSM Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0004",
                  "sku_name": "PET -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0003",
                  "sku_name": "PET -POSM Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0002",
                  "sku_name": "PET -POSM Khung Men",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_004",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "HBM"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B M",
              "skus": [
                {
                  "sku_code": "CMDPOSM0018",
                  "sku_name": "Window Frame -POSM Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0017",
                  "sku_name": "Window Frame -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0016",
                  "sku_name": "Window Frame -POSM Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0005",
                  "sku_name": "PET -POSM Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0004",
                  "sku_name": "PET -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0003",
                  "sku_name": "PET -POSM Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_005",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "HBSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B S & XS",
              "skus": [
                {
                  "sku_code": "CMDPOSM0017",
                  "sku_name": "Window Frame -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0004",
                  "sku_name": "PET -POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_006",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "MP"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P",
              "skus": [
                {
                  "sku_code": "CMDPOSM0022",
                  "sku_name": "Window Frame-POSM PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0019",
                  "sku_name": "Window Frame-POSM HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0007",
                  "sku_name": "PET-POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0006",
                  "sku_name": "PET-POSM Khung HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0010",
                  "sku_name": "POSM GE/FSU",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_007",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "MXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P XS",
              "skus": [
                {
                  "sku_code": "CMDPOSM0010",
                  "sku_name": "POSM GE/FSU",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0022",
                  "sku_name": "Window Frame-POSM PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0007",
                  "sku_name": "PET-POSM Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_008",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "MS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "MS",
              "skus": [
                {
                  "sku_code": "CMDPOSM0020",
                  "sku_name": "Window Frame-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0008",
                  "sku_name": "PET-POSM Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_POSM_009",
          "planogram_name": "Lắp đặt POSM",
          "image_type_id": ["117","118"],
          "region": [],
          "store_types": [
            "MASSIVEOCD"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "Massive & OCD",
              "skus": [
                {
                  "sku_code": "CMDPOSM0012",
                  "sku_name": "POSM Kệ200MBànchải",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0011",
                  "sku_name": "POSM Kệ15MComfort",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0014",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Trụ tròn",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDPOSM0013",
                  "sku_name": "Sachet (dầu dây/vỉ treo Knorr)-POSM Thanh sắt (Bao gồm vỉ treo)",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_001",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "FGSUPERL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (Super & L)",
              "skus": [
                {
                  "sku_code": "CMDWIN0002",
                  "sku_name": "Win HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0009",
                  "sku_name": "Win PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0008",
                  "sku_name": "Win Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0007",
                  "sku_name": "Win Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0001",
                  "sku_name": "Win GE",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win Sachet",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0011",
                  "sku_name": "Win Ụ đảo",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_002",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "FGSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "FG (S & XS)",
              "skus": [
                {
                  "sku_code": "CMDWIN0002",
                  "sku_name": "Win HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0009",
                  "sku_name": "Win PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0008",
                  "sku_name": "Win Lipton",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0007",
                  "sku_name": "Win Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0001",
                  "sku_name": "Win GE",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_003",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "HBL"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B L",
              "skus": [
                {
                  "sku_code": "CMDWIN0006",
                  "sku_name": "Win Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0004",
                  "sku_name": "Win Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0003",
                  "sku_name": "Win Khung Men",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0005",
                  "sku_name": "Win Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_004",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "HBM"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B M",
              "skus": [
                {
                  "sku_code": "CMDWIN0005",
                  "sku_name": "Win Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0006",
                  "sku_name": "Win Khung Skin",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0004",
                  "sku_name": "Win Khung Oral",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_005",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "HBSXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "H&B S & XS",
              "skus": [
                {
                  "sku_code": "CMDWIN0005",
                  "sku_name": "Win Khung PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_006",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "MP"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P",
              "skus": [
                {
                  "sku_code": "CMDWIN0009",
                  "sku_name": "Win PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0002",
                  "sku_name": "Win HC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_007",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "MXS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "M&P XS",
              "skus": [
                {
                  "sku_code": "CMDWIN0009",
                  "sku_name": "Win PC",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win Sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        },
        {
          "planogram_id": "PLG_WIN_008",
          "planogram_name": "Win vị trí",
          "image_type_id": ["119","120"],
          "region": [],
          "store_types": [
            "MS"
          ],
          "value": 'null',
          "options": [
            {
              "label": "Thành công",
              "value": 1
            },
            {
              "label": "Không thành công",
              "value": 0
            }
          ],
          "groups": [
            {
              "group_id": 1,
              "group_name": "MS",
              "skus": [
                {
                  "sku_code": "CMDWIN0007",
                  "sku_name": "Win Knorr",
                  "facing": 1,
                  "value": 'null'
                },
                {
                  "sku_code": "CMDWIN0010",
                  "sku_name": "Win sachet",
                  "facing": 1,
                  "value": 'null'
                }
              ]
            }
          ]
        }
      ]
    },
    "NOTE_UNSUCCESS": {
      "issue_name": "Note Unsuccess",
      "issue_key": "NOTE_UNSUCCESS",
      "done": 'false',
      "store_status": [
        "UNSUCCESS"
      ],
      "validate": {
        "required": 'true'
      },
      "items": [
        {
          "component_type": "TEXT",
          "keyboard_type": "default",
          "component_code": "note_ktc",
          "label": "Lý do Không thành công",
          "validate": {
            "required": 'true'
          },
          "default_value": 'null',
          "value": 'null',
          "childs": []
        }
      ]
    },
    "CHECKOUT": {
      "issue_name": "Check out",
      "issue_key": "CHECKOUT",
      "done": 'false',
      "store_status": [
        "SUCCESS",
        "UNSUCCESS"
      ],
      "validate": {
        "required": 'true'
      },
      "value": {
        "lat": 'null',
        "lng": 'null'
      }
    }
  }
}