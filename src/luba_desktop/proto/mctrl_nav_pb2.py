# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mctrl_nav.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import luba_desktop.proto.common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmctrl_nav.proto\x1a\x0c\x63ommon.proto\"\x84\x0f\n\x07MctlNav\x12$\n\x0ctoapp_lat_up\x18\x01 \x01(\x0b\x32\x0c.NavLatLonUpH\x00\x12!\n\x0ctoapp_pos_up\x18\x02 \x01(\x0b\x32\t.NavPosUpH\x00\x12.\n\x13todev_chl_line_data\x18\x03 \x01(\x0b\x32\x0f.NavCHlLineDataH\x00\x12\'\n\x0ftoapp_task_info\x18\x04 \x01(\x0b\x32\x0c.NavTaskInfoH\x00\x12*\n\x11toapp_opt_line_up\x18\x05 \x01(\x0b\x32\r.NavOptLineUpH\x00\x12\x33\n\x15toapp_opt_border_info\x18\x06 \x01(\x0b\x32\x12.NavOptiBorderInfoH\x00\x12,\n\x12toapp_opt_obs_info\x18\x07 \x01(\x0b\x32\x0e.NavOptObsInfoH\x00\x12+\n\x13todev_task_info_ack\x18\x08 \x01(\x0b\x32\x0c.NavResFrameH\x00\x12\x31\n\x19todev_opt_border_info_ack\x18\t \x01(\x0b\x32\x0c.NavResFrameH\x00\x12.\n\x16todev_opt_obs_info_ack\x18\n \x01(\x0b\x32\x0c.NavResFrameH\x00\x12-\n\x15todev_opt_line_up_ack\x18\x0b \x01(\x0b\x32\x0c.NavResFrameH\x00\x12*\n\x0ftoapp_chgpileto\x18\x0c \x01(\x0b\x32\x0f.chargePileTypeH\x00\x12\x17\n\rtodev_sustask\x18\r \x01(\x05H\x00\x12\x18\n\x0etodev_rechgcmd\x18\x0e \x01(\x05H\x00\x12\x17\n\rtodev_edgecmd\x18\x0f \x01(\x05H\x00\x12\x1b\n\x11todev_draw_border\x18\x10 \x01(\x05H\x00\x12\x1f\n\x15todev_draw_border_end\x18\x11 \x01(\x05H\x00\x12\x18\n\x0etodev_draw_obs\x18\x12 \x01(\x05H\x00\x12\x1c\n\x12todev_draw_obs_end\x18\x13 \x01(\x05H\x00\x12\x18\n\x0etodev_chl_line\x18\x14 \x01(\x05H\x00\x12\x1c\n\x12todev_chl_line_end\x18\x15 \x01(\x05H\x00\x12\x19\n\x0ftodev_save_task\x18\x16 \x01(\x05H\x00\x12\x1d\n\x13todev_cancel_suscmd\x18\x17 \x01(\x05H\x00\x12\x1e\n\x14todev_reset_chg_pile\x18\x18 \x01(\x05H\x00\x12\x1f\n\x15todev_cancel_draw_cmd\x18\x19 \x01(\x05H\x00\x12$\n\x1atodev_one_touch_leave_pile\x18\x1a \x01(\x05H\x00\x12&\n\x0etodev_mow_task\x18\x1b \x01(\x0b\x32\x0c.NavStartJobH\x00\x12\'\n\x0ctoapp_bstate\x18\x1c \x01(\x0b\x32\x0f.NavBorderStateH\x00\x12\x1a\n\x10todev_lat_up_ack\x18\x1d \x01(\x05H\x00\x12(\n\rtodev_gethash\x18\x1e \x01(\x0b\x32\x0f.NavGetHashListH\x00\x12/\n\x11toapp_gethash_ack\x18\x1f \x01(\x0b\x32\x12.NavGetHashListAckH\x00\x12/\n\x14todev_get_commondata\x18  \x01(\x0b\x32\x0f.NavGetCommDataH\x00\x12\x36\n\x18toapp_get_commondata_ack\x18! \x01(\x0b\x32\x12.NavGetCommDataAckH\x00\x12\x31\n\x15\x62idire_reqconver_path\x18\" \x01(\x0b\x32\x10.NavReqCoverPathH\x00\x12.\n\x0ctoapp_zigzag\x18# \x01(\x0b\x32\x16.NavUploadZigZagResultH\x00\x12\x35\n\x10todev_zigzag_ack\x18$ \x01(\x0b\x32\x19.NavUploadZigZagResultAckH\x00\x12&\n\x0etodev_taskctrl\x18% \x01(\x0b\x32\x0c.NavTaskCtrlH\x00\x12%\n\rbidire_taskid\x18& \x01(\x0b\x32\x0c.NavTaskIdRwH\x00\x12&\n\x08toapp_bp\x18\' \x01(\x0b\x32\x12.NavTaskBreakPointH\x00\x12+\n\x11todev_planjob_set\x18( \x01(\x0b\x32\x0e.NavPlanJobSetH\x00\x12\x32\n\x15todev_unable_time_set\x18) \x01(\x0b\x32\x11.NavUnableTimeSetH\x00\x12,\n\x0esimulation_cmd\x18* \x01(\x0b\x32\x12.SimulationCmdDataH\x00\x12<\n\x1ctodev_work_report_update_cmd\x18+ \x01(\x0b\x32\x14.WorkReportUpdateCmdH\x00\x12<\n\x1ctoapp_work_report_update_ack\x18, \x01(\x0b\x32\x14.WorkReportUpdateAckH\x00\x12\x33\n\x15todev_work_report_cmd\x18- \x01(\x0b\x32\x12.WorkReportCmdDataH\x00\x12\x33\n\x15toapp_work_report_ack\x18. \x01(\x0b\x32\x12.WorkReportInfoAckH\x00\x42\x0b\n\tsubNavMsg\"J\n\x10NavBorderDataGet\x12\x14\n\x0c\x63urrentFrame\x18\x02 \x01(\x05\x12\x11\n\tborderLen\x18\x03 \x01(\x05\x12\r\n\x05jobId\x18\x01 \x01(\x05\":\n\x13NavBorderDataGetAck\x12\r\n\x05jobId\x18\x01 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x02 \x01(\x05\"G\n\x18NavObstiBorderDataGetAck\x12\x15\n\robstacleIndex\x18\x01 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x02 \x01(\x05\"d\n\x0eNavCHlLineData\x12\x16\n\x0e\x63hannelLineLen\x18\x04 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x03 \x01(\x05\x12\x10\n\x08\x65ndJobRI\x18\x02 \x01(\x05\x12\x12\n\nstartJobRI\x18\x01 \x01(\x05\"O\n\x11NavCHlLineDataAck\x12\x14\n\x0c\x63urrentFrame\x18\x03 \x01(\x05\x12\x10\n\x08\x65ndJobRI\x18\x02 \x01(\x05\x12\x12\n\nstartJobRI\x18\x01 \x01(\x05\"Z\n\x15NavObstiBorderDataGet\x12\x15\n\robstacleIndex\x18\x01 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x02 \x01(\x05\x12\x14\n\x0cobstaclesLen\x18\x03 \x01(\x05\"\x7f\n\x0bNavTaskInfo\x12\x10\n\x08\x61llFrame\x18\x03 \x01(\x05\x12\x0c\n\x04\x61rea\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x04 \x01(\x05\x12\x0f\n\x07pathlen\x18\x05 \x01(\x05\x12\x1b\n\x02\x64\x63\x18\x06 \x03(\x0b\x32\x0f.CommDataCouple\"\x91\x01\n\x0cNavOptLineUp\x12\x10\n\x08\x65ndJobRI\x18\x02 \x01(\x05\x12\x12\n\nstartJobRI\x18\x01 \x01(\x05\x12\x10\n\x08\x61llFrame\x18\x03 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x04 \x01(\x05\x12\x16\n\x0e\x63hannelDataLen\x18\x05 \x01(\x05\x12\x1b\n\x02\x64\x63\x18\x06 \x03(\x0b\x32\x0f.CommDataCouple\"~\n\x11NavOptiBorderInfo\x12\r\n\x05jobId\x18\x01 \x01(\x05\x12\x10\n\x08\x61llFrame\x18\x02 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x03 \x01(\x05\x12\x15\n\rborderDataLen\x18\x04 \x01(\x05\x12\x1b\n\x02\x64\x63\x18\x05 \x03(\x0b\x32\x0f.CommDataCouple\"\x81\x01\n\rNavOptObsInfo\x12\x12\n\nobstacleId\x18\x01 \x01(\x05\x12\x10\n\x08\x61llFrame\x18\x02 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x03 \x01(\x05\x12\x17\n\x0fobstacleDataLen\x18\x04 \x01(\x05\x12\x1b\n\x02\x64\x63\x18\x05 \x03(\x0b\x32\x0f.CommDataCouple\"\xb4\x01\n\x0bNavStartJob\x12\r\n\x05jobId\x18\x01 \x01(\x03\x12\x0e\n\x06jobVer\x18\x02 \x01(\x05\x12\x0f\n\x07jobMode\x18\x03 \x01(\x05\x12\x13\n\x0brainTactics\x18\x04 \x01(\x05\x12\x13\n\x0bknifeHeight\x18\x05 \x01(\x05\x12\r\n\x05speed\x18\x06 \x01(\x02\x12\x14\n\x0c\x63hannelWidth\x18\x07 \x01(\x05\x12\x11\n\tultraWave\x18\x08 \x01(\x05\x12\x13\n\x0b\x63hannelMode\x18\t \x01(\x05\"|\n\x0eNavGetHashList\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x12\n\ntotalFrame\x18\x03 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x04 \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\x05 \x01(\x03\x12\x10\n\x08reserved\x18\x06 \x01(\t\"\xa4\x01\n\x11NavGetHashListAck\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x12\n\ntotalFrame\x18\x03 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x04 \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\x05 \x01(\x03\x12\x0f\n\x07hashLen\x18\x06 \x01(\x05\x12\x10\n\x08reserved\x18\x07 \x01(\t\x12\x12\n\ndataCouple\x18\r \x03(\x03\"\xd6\x01\n\x0eNavGetCommData\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0c\n\x04hash\x18\x05 \x01(\x03\x12\x15\n\rpaternalHashA\x18\x06 \x01(\x03\x12\x15\n\rpaternalHashB\x18\x07 \x01(\x03\x12\x12\n\ntotalFrame\x18\x08 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\t \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\n \x01(\x03\x12\x10\n\x08reserved\x18\x0b \x01(\t\"\x9f\x02\n\x11NavGetCommDataAck\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x0e\n\x06result\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\x05\x12\x0c\n\x04type\x18\x05 \x01(\x05\x12\x0c\n\x04hash\x18\x06 \x01(\x03\x12\x15\n\rpaternalHashA\x18\x07 \x01(\x03\x12\x15\n\rpaternalHashB\x18\x08 \x01(\x03\x12\x12\n\ntotalFrame\x18\t \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\n \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\x0b \x01(\x03\x12\x0f\n\x07\x64\x61taLen\x18\x0c \x01(\x05\x12#\n\ndataCouple\x18\r \x03(\x0b\x32\x0f.CommDataCouple\x12\x10\n\x08reserved\x18\x0e \x01(\t\"\xaa\x02\n\x0fNavReqCoverPath\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\r\n\x05jobId\x18\x02 \x01(\x03\x12\x0e\n\x06jobVer\x18\x03 \x01(\x05\x12\x0f\n\x07jobMode\x18\x04 \x01(\x05\x12\x0e\n\x06subCmd\x18\x05 \x01(\x05\x12\x10\n\x08\x65\x64geMode\x18\x06 \x01(\x05\x12\x13\n\x0bknifeHeight\x18\x07 \x01(\x05\x12\x14\n\x0c\x63hannelWidth\x18\x08 \x01(\x05\x12\x11\n\tultraWave\x18\t \x01(\x05\x12\x13\n\x0b\x63hannelMode\x18\n \x01(\x05\x12\x0e\n\x06toward\x18\x0b \x01(\x05\x12\r\n\x05speed\x18\x0c \x01(\x02\x12\x11\n\tzoneHashs\x18\r \x03(\x03\x12\x10\n\x08pathHash\x18\x0e \x01(\x03\x12\x10\n\x08reserved\x18\x0f \x01(\t\x12\x0e\n\x06result\x18\x10 \x01(\x05\"\x97\x03\n\x15NavUploadZigZagResult\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\r\n\x05jobId\x18\x02 \x01(\x03\x12\x0e\n\x06jobVer\x18\x03 \x01(\x05\x12\x0e\n\x06result\x18\x04 \x01(\x05\x12\x0c\n\x04\x61rea\x18\x05 \x01(\x05\x12\x0c\n\x04time\x18\x06 \x01(\x05\x12\x14\n\x0ctotalZoneNum\x18\x07 \x01(\x05\x12\x1a\n\x12\x63urrentZonePathNum\x18\x08 \x01(\x05\x12\x19\n\x11\x63urrentZonePathId\x18\t \x01(\x05\x12\x13\n\x0b\x63urrentZone\x18\n \x01(\x05\x12\x13\n\x0b\x63urrentHash\x18\x0b \x01(\x03\x12\x12\n\ntotalFrame\x18\x0c \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\r \x01(\x05\x12\x13\n\x0b\x63hannelMode\x18\x0e \x01(\x05\x12\x15\n\rchannelModeId\x18\x0f \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\x10 \x01(\x03\x12\x0f\n\x07\x64\x61taLen\x18\x11 \x01(\x05\x12\x10\n\x08reserved\x18\x12 \x01(\t\x12#\n\ndataCouple\x18\x13 \x03(\x0b\x32\x0f.CommDataCouple\"\xb0\x01\n\x18NavUploadZigZagResultAck\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x13\n\x0b\x63urrentZone\x18\x02 \x01(\x05\x12\x13\n\x0b\x63urrentHash\x18\x03 \x01(\x03\x12\x12\n\ntotalFrame\x18\x04 \x01(\x05\x12\x14\n\x0c\x63urrentFrame\x18\x05 \x01(\x05\x12\x10\n\x08\x64\x61taHash\x18\x06 \x01(\x03\x12\x10\n\x08reserved\x18\x07 \x01(\t\x12\x0e\n\x06subCmd\x18\x08 \x01(\x05\"M\n\x0bNavTaskCtrl\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\x12\x0e\n\x06result\x18\x03 \x01(\x05\x12\x10\n\x08reserved\x18\x04 \x01(\x05\"o\n\x0bNavTaskIdRw\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x10\n\x08taskName\x18\x03 \x01(\t\x12\x0e\n\x06taskId\x18\x04 \x01(\t\x12\x0e\n\x06result\x18\x05 \x01(\x05\x12\x10\n\x08reserved\x18\x06 \x01(\t\"J\n\x12NavSysHashOverview\x12\x1a\n\x12\x63ommonhashOverview\x18\x01 \x01(\x03\x12\x18\n\x10pathHashOverview\x18\x02 \x01(\x03\"i\n\x11NavTaskBreakPoint\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0e\n\x06toward\x18\x03 \x01(\x05\x12\x0c\n\x04\x66lag\x18\x04 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\x05\x12\x10\n\x08zoneHash\x18\x06 \x01(\x03\"\xa2\x04\n\rNavPlanJobSet\x12\x0c\n\x04pver\x18\x01 \x01(\x05\x12\x0e\n\x06subCmd\x18\x02 \x01(\x05\x12\x0c\n\x04\x61rea\x18\x03 \x01(\x05\x12\x10\n\x08workTime\x18\x04 \x01(\x05\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x0e\n\x06userId\x18\x07 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x08 \x01(\t\x12\x0e\n\x06planId\x18\t \x01(\t\x12\x0e\n\x06taskId\x18\n \x01(\t\x12\r\n\x05jobId\x18\x0b \x01(\t\x12\x11\n\tstartTime\x18\x0c \x01(\t\x12\x0f\n\x07\x65ndTime\x18\r \x01(\t\x12\x0c\n\x04week\x18\x0e \x01(\x05\x12\x13\n\x0bknifeHeight\x18\x0f \x01(\x05\x12\r\n\x05model\x18\x10 \x01(\x05\x12\x10\n\x08\x65\x64geMode\x18\x11 \x01(\x05\x12\x14\n\x0crequiredTime\x18\x12 \x01(\x05\x12\x12\n\nrouteAngle\x18\x13 \x01(\x05\x12\x12\n\nrouteModel\x18\x14 \x01(\x05\x12\x14\n\x0crouteSpacing\x18\x15 \x01(\x05\x12\x19\n\x11ultrasonicBarrier\x18\x16 \x01(\x05\x12\x14\n\x0ctotalPlanNum\x18\x17 \x01(\x05\x12\x11\n\tplanIndex\x18\x18 \x01(\x05\x12\x0e\n\x06result\x18\x19 \x01(\x05\x12\r\n\x05speed\x18\x1a \x01(\x02\x12\x10\n\x08taskName\x18\x1b \x01(\t\x12\x0f\n\x07jobName\x18\x1c \x01(\t\x12\x11\n\tzoneHashs\x18\x1d \x03(\x03\x12\x10\n\x08reserved\x18\x1e \x01(\t\")\n\x0bNavLatLonUp\x12\x0c\n\x04lat_\x18\x01 \x01(\x01\x12\x0c\n\x04lon_\x18\x02 \x01(\x01\"\xc9\x01\n\x08NavPosUp\x12\x0b\n\x03\x61ge\x18\x06 \x01(\x02\x12\x0f\n\x07\x63HashId\x18\x0b \x01(\x03\x12\x11\n\tl2DfStars\x18\t \x01(\x05\x12\x11\n\tlatStddev\x18\x07 \x01(\x02\x12\x11\n\tlonStddev\x18\x08 \x01(\x02\x12\x10\n\x08posLevel\x18\x0c \x01(\x05\x12\x0f\n\x07posType\x18\n \x01(\x05\x12\r\n\x05stars\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0e\n\x06toward\x18\x04 \x01(\x05\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\"\"\n\x0eNavBorderState\x12\x10\n\x08\x62\x64state_\x18\x01 \x01(\x05\"\x1e\n\x0bNavResFrame\x12\x0f\n\x07\x66rameId\x18\x01 \x01(\x05\"\'\n\x0fNavTaskProgress\x12\x14\n\x0ctaskProgress\x18\x01 \x01(\x05\"\x86\x01\n\x10NavUnableTimeSet\x12\x0e\n\x06subCmd\x18\x01 \x01(\x05\x12\x10\n\x08\x64\x65viceId\x18\x02 \x01(\t\x12\x17\n\x0funableStartTime\x18\x03 \x01(\t\x12\x15\n\runableEndTime\x18\x04 \x01(\t\x12\x0e\n\x06result\x18\x05 \x01(\x05\x12\x10\n\x08reserved\x18\x06 \x01(\t\"H\n\x11SimulationCmdData\x12\x0e\n\x06subCmd\x18\x01 \x01(\x05\x12\x0f\n\x07paramId\x18\x02 \x01(\x05\x12\x12\n\nparamValue\x18\x03 \x03(\x05\"7\n\x11WorkReportCmdData\x12\x0e\n\x06subCmd\x18\x01 \x01(\x05\x12\x12\n\ngetInfoNum\x18\x02 \x01(\x05\"\xfd\x01\n\x11WorkReportInfoAck\x12\x15\n\rcurrentAckNum\x18\x01 \x01(\x05\x12\x13\n\x0b\x65ndWorkTime\x18\x02 \x01(\x03\x12\x15\n\rheightOfKnife\x18\x03 \x01(\x05\x12\x15\n\rinterruptFlag\x18\x04 \x01(\x08\x12\x15\n\rstartWorkTime\x18\x05 \x01(\x03\x12\x13\n\x0btotalAckNum\x18\x06 \x01(\x05\x12\x10\n\x08workAres\x18\x07 \x01(\x01\x12\x14\n\x0cworkProgress\x18\x08 \x01(\x05\x12\x12\n\nworkResult\x18\t \x01(\x05\x12\x14\n\x0cworkTimeUsed\x18\n \x01(\x05\x12\x10\n\x08workType\x18\x0b \x01(\x05\":\n\x13WorkReportUpdateAck\x12\x0f\n\x07infoNum\x18\x02 \x01(\x05\x12\x12\n\nupdateFlag\x18\x01 \x01(\x08\"%\n\x13WorkReportUpdateCmd\x12\x0e\n\x06subCmd\x18\x01 \x01(\x05\"6\n\x0e\x63hargePileType\x12\x0e\n\x06toward\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mctrl_nav_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MCTLNAV']._serialized_start=34
  _globals['_MCTLNAV']._serialized_end=1958
  _globals['_NAVBORDERDATAGET']._serialized_start=1960
  _globals['_NAVBORDERDATAGET']._serialized_end=2034
  _globals['_NAVBORDERDATAGETACK']._serialized_start=2036
  _globals['_NAVBORDERDATAGETACK']._serialized_end=2094
  _globals['_NAVOBSTIBORDERDATAGETACK']._serialized_start=2096
  _globals['_NAVOBSTIBORDERDATAGETACK']._serialized_end=2167
  _globals['_NAVCHLLINEDATA']._serialized_start=2169
  _globals['_NAVCHLLINEDATA']._serialized_end=2269
  _globals['_NAVCHLLINEDATAACK']._serialized_start=2271
  _globals['_NAVCHLLINEDATAACK']._serialized_end=2350
  _globals['_NAVOBSTIBORDERDATAGET']._serialized_start=2352
  _globals['_NAVOBSTIBORDERDATAGET']._serialized_end=2442
  _globals['_NAVTASKINFO']._serialized_start=2444
  _globals['_NAVTASKINFO']._serialized_end=2571
  _globals['_NAVOPTLINEUP']._serialized_start=2574
  _globals['_NAVOPTLINEUP']._serialized_end=2719
  _globals['_NAVOPTIBORDERINFO']._serialized_start=2721
  _globals['_NAVOPTIBORDERINFO']._serialized_end=2847
  _globals['_NAVOPTOBSINFO']._serialized_start=2850
  _globals['_NAVOPTOBSINFO']._serialized_end=2979
  _globals['_NAVSTARTJOB']._serialized_start=2982
  _globals['_NAVSTARTJOB']._serialized_end=3162
  _globals['_NAVGETHASHLIST']._serialized_start=3164
  _globals['_NAVGETHASHLIST']._serialized_end=3288
  _globals['_NAVGETHASHLISTACK']._serialized_start=3291
  _globals['_NAVGETHASHLISTACK']._serialized_end=3455
  _globals['_NAVGETCOMMDATA']._serialized_start=3458
  _globals['_NAVGETCOMMDATA']._serialized_end=3672
  _globals['_NAVGETCOMMDATAACK']._serialized_start=3675
  _globals['_NAVGETCOMMDATAACK']._serialized_end=3962
  _globals['_NAVREQCOVERPATH']._serialized_start=3965
  _globals['_NAVREQCOVERPATH']._serialized_end=4263
  _globals['_NAVUPLOADZIGZAGRESULT']._serialized_start=4266
  _globals['_NAVUPLOADZIGZAGRESULT']._serialized_end=4673
  _globals['_NAVUPLOADZIGZAGRESULTACK']._serialized_start=4676
  _globals['_NAVUPLOADZIGZAGRESULTACK']._serialized_end=4852
  _globals['_NAVTASKCTRL']._serialized_start=4854
  _globals['_NAVTASKCTRL']._serialized_end=4931
  _globals['_NAVTASKIDRW']._serialized_start=4933
  _globals['_NAVTASKIDRW']._serialized_end=5044
  _globals['_NAVSYSHASHOVERVIEW']._serialized_start=5046
  _globals['_NAVSYSHASHOVERVIEW']._serialized_end=5120
  _globals['_NAVTASKBREAKPOINT']._serialized_start=5122
  _globals['_NAVTASKBREAKPOINT']._serialized_end=5227
  _globals['_NAVPLANJOBSET']._serialized_start=5230
  _globals['_NAVPLANJOBSET']._serialized_end=5776
  _globals['_NAVLATLONUP']._serialized_start=5778
  _globals['_NAVLATLONUP']._serialized_end=5819
  _globals['_NAVPOSUP']._serialized_start=5822
  _globals['_NAVPOSUP']._serialized_end=6023
  _globals['_NAVBORDERSTATE']._serialized_start=6025
  _globals['_NAVBORDERSTATE']._serialized_end=6059
  _globals['_NAVRESFRAME']._serialized_start=6061
  _globals['_NAVRESFRAME']._serialized_end=6091
  _globals['_NAVTASKPROGRESS']._serialized_start=6093
  _globals['_NAVTASKPROGRESS']._serialized_end=6132
  _globals['_NAVUNABLETIMESET']._serialized_start=6135
  _globals['_NAVUNABLETIMESET']._serialized_end=6269
  _globals['_SIMULATIONCMDDATA']._serialized_start=6271
  _globals['_SIMULATIONCMDDATA']._serialized_end=6343
  _globals['_WORKREPORTCMDDATA']._serialized_start=6345
  _globals['_WORKREPORTCMDDATA']._serialized_end=6400
  _globals['_WORKREPORTINFOACK']._serialized_start=6403
  _globals['_WORKREPORTINFOACK']._serialized_end=6656
  _globals['_WORKREPORTUPDATEACK']._serialized_start=6658
  _globals['_WORKREPORTUPDATEACK']._serialized_end=6716
  _globals['_WORKREPORTUPDATECMD']._serialized_start=6718
  _globals['_WORKREPORTUPDATECMD']._serialized_end=6755
  _globals['_CHARGEPILETYPE']._serialized_start=6757
  _globals['_CHARGEPILETYPE']._serialized_end=6811
# @@protoc_insertion_point(module_scope)
