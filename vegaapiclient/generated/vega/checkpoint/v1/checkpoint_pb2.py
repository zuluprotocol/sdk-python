# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vega/checkpoint/v1/checkpoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ... import vega_pb2 as vega_dot_vega__pb2
from ... import assets_pb2 as vega_dot_assets__pb2
from ... import governance_pb2 as vega_dot_governance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vega/checkpoint/v1/checkpoint.proto',
  package='vega.checkpoint.v1',
  syntax='proto3',
  serialized_options=b'Z.code.vegaprotocol.io/protos/vega/checkpoint/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#vega/checkpoint/v1/checkpoint.proto\x12\x12vega.checkpoint.v1\x1a\x0fvega/vega.proto\x1a\x11vega/assets.proto\x1a\x15vega/governance.proto\";\n\x0f\x43heckpointState\x12\x12\n\x04hash\x18\x01 \x01(\x0cR\x04hash\x12\x14\n\x05state\x18\x02 \x01(\x0cR\x05state\"\x9e\x02\n\nCheckpoint\x12\x1e\n\ngovernance\x18\x01 \x01(\x0cR\ngovernance\x12\x16\n\x06\x61ssets\x18\x02 \x01(\x0cR\x06\x61ssets\x12\x1e\n\ncollateral\x18\x03 \x01(\x0cR\ncollateral\x12-\n\x12network_parameters\x18\x04 \x01(\x0cR\x11networkParameters\x12\x1e\n\ndelegation\x18\x05 \x01(\x0cR\ndelegation\x12\x14\n\x05\x65poch\x18\x06 \x01(\x0cR\x05\x65poch\x12\x14\n\x05\x62lock\x18\x07 \x01(\x0cR\x05\x62lock\x12\x18\n\x07rewards\x18\x08 \x01(\x0cR\x07rewards\x12#\n\rkey_rotations\x18\t \x01(\x0cR\x0ckeyRotations\"U\n\nAssetEntry\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x37\n\rasset_details\x18\x02 \x01(\x0b\x32\x12.vega.AssetDetailsR\x0c\x61ssetDetails\"@\n\x06\x41ssets\x12\x36\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x1e.vega.checkpoint.v1.AssetEntryR\x06\x61ssets\"T\n\x0c\x41ssetBalance\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x14\n\x05\x61sset\x18\x02 \x01(\tR\x05\x61sset\x12\x18\n\x07\x62\x61lance\x18\x03 \x01(\tR\x07\x62\x61lance\"J\n\nCollateral\x12<\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32 .vega.checkpoint.v1.AssetBalanceR\x08\x62\x61lances\";\n\tNetParams\x12.\n\x06params\x18\x01 \x03(\x0b\x32\x16.vega.NetworkParameterR\x06params\"9\n\tProposals\x12,\n\tproposals\x18\x01 \x03(\x0b\x32\x0e.vega.ProposalR\tproposals\"\x8e\x01\n\rDelegateEntry\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x12\n\x04node\x18\x02 \x01(\tR\x04node\x12\x16\n\x06\x61mount\x18\x03 \x01(\tR\x06\x61mount\x12\x1e\n\nundelegate\x18\x04 \x01(\x08R\nundelegate\x12\x1b\n\tepoch_seq\x18\x05 \x01(\x04R\x08\x65pochSeq\"\xab\x01\n\x08\x44\x65legate\x12\x39\n\x06\x61\x63tive\x18\x01 \x03(\x0b\x32!.vega.checkpoint.v1.DelegateEntryR\x06\x61\x63tive\x12;\n\x07pending\x18\x02 \x03(\x0b\x32!.vega.checkpoint.v1.DelegateEntryR\x07pending\x12\'\n\x0f\x61uto_delegation\x18\x03 \x03(\tR\x0e\x61utoDelegation\"\x1f\n\x05\x42lock\x12\x16\n\x06height\x18\x01 \x01(\x03R\x06height\"E\n\x07Rewards\x12:\n\x07rewards\x18\x01 \x03(\x0b\x32 .vega.checkpoint.v1.RewardPayoutR\x07rewards\"\x7f\n\x0cRewardPayout\x12\x1f\n\x0bpayout_time\x18\x01 \x01(\x03R\npayoutTime\x12N\n\x0erewards_payout\x18\x02 \x03(\x0b\x32\'.vega.checkpoint.v1.PendingRewardPayoutR\rrewardsPayout\"\xf0\x01\n\x13PendingRewardPayout\x12!\n\x0c\x66rom_account\x18\x01 \x01(\tR\x0b\x66romAccount\x12\x14\n\x05\x61sset\x18\x02 \x01(\tR\x05\x61sset\x12\x42\n\x0cparty_amount\x18\x03 \x03(\x0b\x32\x1f.vega.checkpoint.v1.PartyAmountR\x0bpartyAmount\x12!\n\x0ctotal_reward\x18\x04 \x01(\tR\x0btotalReward\x12\x1b\n\tepoch_seq\x18\x05 \x01(\tR\x08\x65pochSeq\x12\x1c\n\ttimestamp\x18\x06 \x01(\x03R\ttimestamp\";\n\x0bPartyAmount\x12\x14\n\x05party\x18\x01 \x01(\tR\x05party\x12\x16\n\x06\x61mount\x18\x02 \x01(\tR\x06\x61mount\"\xb9\x01\n\x12PendingKeyRotation\x12?\n\x1crelative_target_block_height\x18\x01 \x01(\x04R\x19relativeTargetBlockHeight\x12\x17\n\x07node_id\x18\x02 \x01(\tR\x06nodeId\x12\x1e\n\x0bnew_pub_key\x18\x03 \x01(\tR\tnewPubKey\x12)\n\x11new_pub_key_index\x18\x04 \x01(\rR\x0enewPubKeyIndex\"j\n\x0cKeyRotations\x12Z\n\x15pending_key_rotations\x18\x01 \x03(\x0b\x32&.vega.checkpoint.v1.PendingKeyRotationR\x13pendingKeyRotationsB0Z.code.vegaprotocol.io/protos/vega/checkpoint/v1b\x06proto3'
  ,
  dependencies=[vega_dot_vega__pb2.DESCRIPTOR,vega_dot_assets__pb2.DESCRIPTOR,vega_dot_governance__pb2.DESCRIPTOR,])




_CHECKPOINTSTATE = _descriptor.Descriptor(
  name='CheckpointState',
  full_name='vega.checkpoint.v1.CheckpointState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='vega.checkpoint.v1.CheckpointState.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hash', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='vega.checkpoint.v1.CheckpointState.state', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=177,
)


_CHECKPOINT = _descriptor.Descriptor(
  name='Checkpoint',
  full_name='vega.checkpoint.v1.Checkpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='governance', full_name='vega.checkpoint.v1.Checkpoint.governance', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='governance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assets', full_name='vega.checkpoint.v1.Checkpoint.assets', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collateral', full_name='vega.checkpoint.v1.Checkpoint.collateral', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='collateral', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_parameters', full_name='vega.checkpoint.v1.Checkpoint.network_parameters', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkParameters', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegation', full_name='vega.checkpoint.v1.Checkpoint.delegation', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delegation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='vega.checkpoint.v1.Checkpoint.epoch', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='epoch', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block', full_name='vega.checkpoint.v1.Checkpoint.block', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='vega.checkpoint.v1.Checkpoint.rewards', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rewards', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_rotations', full_name='vega.checkpoint.v1.Checkpoint.key_rotations', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keyRotations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=466,
)


_ASSETENTRY = _descriptor.Descriptor(
  name='AssetEntry',
  full_name='vega.checkpoint.v1.AssetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='vega.checkpoint.v1.AssetEntry.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset_details', full_name='vega.checkpoint.v1.AssetEntry.asset_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assetDetails', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=553,
)


_ASSETS = _descriptor.Descriptor(
  name='Assets',
  full_name='vega.checkpoint.v1.Assets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='vega.checkpoint.v1.Assets.assets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='assets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=619,
)


_ASSETBALANCE = _descriptor.Descriptor(
  name='AssetBalance',
  full_name='vega.checkpoint.v1.AssetBalance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='vega.checkpoint.v1.AssetBalance.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='party', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='vega.checkpoint.v1.AssetBalance.asset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='vega.checkpoint.v1.AssetBalance.balance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='balance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=705,
)


_COLLATERAL = _descriptor.Descriptor(
  name='Collateral',
  full_name='vega.checkpoint.v1.Collateral',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='balances', full_name='vega.checkpoint.v1.Collateral.balances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='balances', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=781,
)


_NETPARAMS = _descriptor.Descriptor(
  name='NetParams',
  full_name='vega.checkpoint.v1.NetParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='vega.checkpoint.v1.NetParams.params', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=783,
  serialized_end=842,
)


_PROPOSALS = _descriptor.Descriptor(
  name='Proposals',
  full_name='vega.checkpoint.v1.Proposals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposals', full_name='vega.checkpoint.v1.Proposals.proposals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='proposals', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=901,
)


_DELEGATEENTRY = _descriptor.Descriptor(
  name='DelegateEntry',
  full_name='vega.checkpoint.v1.DelegateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='vega.checkpoint.v1.DelegateEntry.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='party', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='vega.checkpoint.v1.DelegateEntry.node', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='vega.checkpoint.v1.DelegateEntry.amount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='undelegate', full_name='vega.checkpoint.v1.DelegateEntry.undelegate', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='undelegate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch_seq', full_name='vega.checkpoint.v1.DelegateEntry.epoch_seq', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='epochSeq', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=904,
  serialized_end=1046,
)


_DELEGATE = _descriptor.Descriptor(
  name='Delegate',
  full_name='vega.checkpoint.v1.Delegate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='active', full_name='vega.checkpoint.v1.Delegate.active', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='active', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending', full_name='vega.checkpoint.v1.Delegate.pending', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auto_delegation', full_name='vega.checkpoint.v1.Delegate.auto_delegation', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='autoDelegation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1049,
  serialized_end=1220,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='vega.checkpoint.v1.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='vega.checkpoint.v1.Block.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='height', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1222,
  serialized_end=1253,
)


_REWARDS = _descriptor.Descriptor(
  name='Rewards',
  full_name='vega.checkpoint.v1.Rewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='vega.checkpoint.v1.Rewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rewards', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1255,
  serialized_end=1324,
)


_REWARDPAYOUT = _descriptor.Descriptor(
  name='RewardPayout',
  full_name='vega.checkpoint.v1.RewardPayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payout_time', full_name='vega.checkpoint.v1.RewardPayout.payout_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payoutTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rewards_payout', full_name='vega.checkpoint.v1.RewardPayout.rewards_payout', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rewardsPayout', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1326,
  serialized_end=1453,
)


_PENDINGREWARDPAYOUT = _descriptor.Descriptor(
  name='PendingRewardPayout',
  full_name='vega.checkpoint.v1.PendingRewardPayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_account', full_name='vega.checkpoint.v1.PendingRewardPayout.from_account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fromAccount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asset', full_name='vega.checkpoint.v1.PendingRewardPayout.asset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='party_amount', full_name='vega.checkpoint.v1.PendingRewardPayout.party_amount', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partyAmount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_reward', full_name='vega.checkpoint.v1.PendingRewardPayout.total_reward', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='totalReward', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch_seq', full_name='vega.checkpoint.v1.PendingRewardPayout.epoch_seq', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='epochSeq', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='vega.checkpoint.v1.PendingRewardPayout.timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1456,
  serialized_end=1696,
)


_PARTYAMOUNT = _descriptor.Descriptor(
  name='PartyAmount',
  full_name='vega.checkpoint.v1.PartyAmount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party', full_name='vega.checkpoint.v1.PartyAmount.party', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='party', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='vega.checkpoint.v1.PartyAmount.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1698,
  serialized_end=1757,
)


_PENDINGKEYROTATION = _descriptor.Descriptor(
  name='PendingKeyRotation',
  full_name='vega.checkpoint.v1.PendingKeyRotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relative_target_block_height', full_name='vega.checkpoint.v1.PendingKeyRotation.relative_target_block_height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='relativeTargetBlockHeight', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='vega.checkpoint.v1.PendingKeyRotation.node_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodeId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_pub_key', full_name='vega.checkpoint.v1.PendingKeyRotation.new_pub_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='newPubKey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_pub_key_index', full_name='vega.checkpoint.v1.PendingKeyRotation.new_pub_key_index', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='newPubKeyIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1760,
  serialized_end=1945,
)


_KEYROTATIONS = _descriptor.Descriptor(
  name='KeyRotations',
  full_name='vega.checkpoint.v1.KeyRotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending_key_rotations', full_name='vega.checkpoint.v1.KeyRotations.pending_key_rotations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pendingKeyRotations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1947,
  serialized_end=2053,
)

_ASSETENTRY.fields_by_name['asset_details'].message_type = vega_dot_assets__pb2._ASSETDETAILS
_ASSETS.fields_by_name['assets'].message_type = _ASSETENTRY
_COLLATERAL.fields_by_name['balances'].message_type = _ASSETBALANCE
_NETPARAMS.fields_by_name['params'].message_type = vega_dot_vega__pb2._NETWORKPARAMETER
_PROPOSALS.fields_by_name['proposals'].message_type = vega_dot_governance__pb2._PROPOSAL
_DELEGATE.fields_by_name['active'].message_type = _DELEGATEENTRY
_DELEGATE.fields_by_name['pending'].message_type = _DELEGATEENTRY
_REWARDS.fields_by_name['rewards'].message_type = _REWARDPAYOUT
_REWARDPAYOUT.fields_by_name['rewards_payout'].message_type = _PENDINGREWARDPAYOUT
_PENDINGREWARDPAYOUT.fields_by_name['party_amount'].message_type = _PARTYAMOUNT
_KEYROTATIONS.fields_by_name['pending_key_rotations'].message_type = _PENDINGKEYROTATION
DESCRIPTOR.message_types_by_name['CheckpointState'] = _CHECKPOINTSTATE
DESCRIPTOR.message_types_by_name['Checkpoint'] = _CHECKPOINT
DESCRIPTOR.message_types_by_name['AssetEntry'] = _ASSETENTRY
DESCRIPTOR.message_types_by_name['Assets'] = _ASSETS
DESCRIPTOR.message_types_by_name['AssetBalance'] = _ASSETBALANCE
DESCRIPTOR.message_types_by_name['Collateral'] = _COLLATERAL
DESCRIPTOR.message_types_by_name['NetParams'] = _NETPARAMS
DESCRIPTOR.message_types_by_name['Proposals'] = _PROPOSALS
DESCRIPTOR.message_types_by_name['DelegateEntry'] = _DELEGATEENTRY
DESCRIPTOR.message_types_by_name['Delegate'] = _DELEGATE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Rewards'] = _REWARDS
DESCRIPTOR.message_types_by_name['RewardPayout'] = _REWARDPAYOUT
DESCRIPTOR.message_types_by_name['PendingRewardPayout'] = _PENDINGREWARDPAYOUT
DESCRIPTOR.message_types_by_name['PartyAmount'] = _PARTYAMOUNT
DESCRIPTOR.message_types_by_name['PendingKeyRotation'] = _PENDINGKEYROTATION
DESCRIPTOR.message_types_by_name['KeyRotations'] = _KEYROTATIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckpointState = _reflection.GeneratedProtocolMessageType('CheckpointState', (_message.Message,), {
  'DESCRIPTOR' : _CHECKPOINTSTATE,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.CheckpointState)
  })
_sym_db.RegisterMessage(CheckpointState)

Checkpoint = _reflection.GeneratedProtocolMessageType('Checkpoint', (_message.Message,), {
  'DESCRIPTOR' : _CHECKPOINT,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Checkpoint)
  })
_sym_db.RegisterMessage(Checkpoint)

AssetEntry = _reflection.GeneratedProtocolMessageType('AssetEntry', (_message.Message,), {
  'DESCRIPTOR' : _ASSETENTRY,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.AssetEntry)
  })
_sym_db.RegisterMessage(AssetEntry)

Assets = _reflection.GeneratedProtocolMessageType('Assets', (_message.Message,), {
  'DESCRIPTOR' : _ASSETS,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Assets)
  })
_sym_db.RegisterMessage(Assets)

AssetBalance = _reflection.GeneratedProtocolMessageType('AssetBalance', (_message.Message,), {
  'DESCRIPTOR' : _ASSETBALANCE,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.AssetBalance)
  })
_sym_db.RegisterMessage(AssetBalance)

Collateral = _reflection.GeneratedProtocolMessageType('Collateral', (_message.Message,), {
  'DESCRIPTOR' : _COLLATERAL,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Collateral)
  })
_sym_db.RegisterMessage(Collateral)

NetParams = _reflection.GeneratedProtocolMessageType('NetParams', (_message.Message,), {
  'DESCRIPTOR' : _NETPARAMS,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.NetParams)
  })
_sym_db.RegisterMessage(NetParams)

Proposals = _reflection.GeneratedProtocolMessageType('Proposals', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSALS,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Proposals)
  })
_sym_db.RegisterMessage(Proposals)

DelegateEntry = _reflection.GeneratedProtocolMessageType('DelegateEntry', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATEENTRY,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.DelegateEntry)
  })
_sym_db.RegisterMessage(DelegateEntry)

Delegate = _reflection.GeneratedProtocolMessageType('Delegate', (_message.Message,), {
  'DESCRIPTOR' : _DELEGATE,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Delegate)
  })
_sym_db.RegisterMessage(Delegate)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Block)
  })
_sym_db.RegisterMessage(Block)

Rewards = _reflection.GeneratedProtocolMessageType('Rewards', (_message.Message,), {
  'DESCRIPTOR' : _REWARDS,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.Rewards)
  })
_sym_db.RegisterMessage(Rewards)

RewardPayout = _reflection.GeneratedProtocolMessageType('RewardPayout', (_message.Message,), {
  'DESCRIPTOR' : _REWARDPAYOUT,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.RewardPayout)
  })
_sym_db.RegisterMessage(RewardPayout)

PendingRewardPayout = _reflection.GeneratedProtocolMessageType('PendingRewardPayout', (_message.Message,), {
  'DESCRIPTOR' : _PENDINGREWARDPAYOUT,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.PendingRewardPayout)
  })
_sym_db.RegisterMessage(PendingRewardPayout)

PartyAmount = _reflection.GeneratedProtocolMessageType('PartyAmount', (_message.Message,), {
  'DESCRIPTOR' : _PARTYAMOUNT,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.PartyAmount)
  })
_sym_db.RegisterMessage(PartyAmount)

PendingKeyRotation = _reflection.GeneratedProtocolMessageType('PendingKeyRotation', (_message.Message,), {
  'DESCRIPTOR' : _PENDINGKEYROTATION,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.PendingKeyRotation)
  })
_sym_db.RegisterMessage(PendingKeyRotation)

KeyRotations = _reflection.GeneratedProtocolMessageType('KeyRotations', (_message.Message,), {
  'DESCRIPTOR' : _KEYROTATIONS,
  '__module__' : 'vega.checkpoint.v1.checkpoint_pb2'
  # @@protoc_insertion_point(class_scope:vega.checkpoint.v1.KeyRotations)
  })
_sym_db.RegisterMessage(KeyRotations)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
