#!/usr/bin/env bash

generated_dir="${GENERATED_DIR:?}"

mv "$generated_dir/github.com/mwitkow/go_proto_validators/validator_pb2_grpc.py" "$generated_dir/github/com/mwitkow/go_proto_validators/"
rm -rf "$generated_dir/github.com"

for x in \
	github/com/mwitkow/go_proto_validators \
	data_node/api/v1 \
	vega/api \
	vega/checkpoint/v1 \
	vega/commands/v1 \
	vega/coreapi/v1 \
	vega/events/v1 \
	vega/oracles/v1 \
	vega/snapshot/v1 \
	vega/tm \
	vega/wallet/v1
do
	# from . import XX as XX
	pb_py="$(find "$generated_dir/$x/" -maxdepth 1 -name '*_pb2.py' -o -name '*_pb2_grpc.py' -o -type d | sort | tail -n +2)"
	(
		echo "$pb_py" | while read -r pb ; do
			if test -f "$pb" ; then
				imp="$(basename "${pb//.py/}")"
				echo "from . import $imp as ${imp/_pb2/}"
			elif test -d "$pb" ; then
				imp="$(basename "$pb")"
				echo "from . import $imp"
			else
				echo "# Ignoring: $pb"
			fi
		done
		echo
	) > "$generated_dir/$x/__init__.py"

	# __all__ = [...]
	(
		echo "__all__ = ["
		echo "$pb_py" | while read -r pb ; do
			if test -f "$pb" ; then
				imp="$(basename "${pb//.py/}")"
				echo "    \"${imp/_pb2/}\","
			elif test -d "$pb" ; then
				imp="$(basename "$pb")"
				echo "    \"$imp\","
			else
				echo "# Ignoring: $pb"
			fi
		done
		echo "]"
	) >> "$generated_dir/$x/__init__.py"
done

for x in \
	data_node/api \
	vega/checkpoint \
	vega/commands \
	vega/coreapi \
	vega/events \
	vega/oracles \
	vega/snapshot \
	vega/wallet
do
	cat >"$generated_dir/$x/__init__.py" <<EOF
from . import v1

__all__ = ["v1"]
EOF
done

cat >"$generated_dir/data_node/__init__.py" <<EOF
from . import api

__all__ = ["api"]
EOF

python3 generate_vega_init.py >"$generated_dir/vega/__init__.py"

cat >"$generated_dir/__init__.py" <<EOF
from . import data_node, github, vega

__all__ = ["data_node", "github", "vega"]
EOF

for x in \
	. \
	github \
	github/com \
	github/com/mwitkow \
	vega/checkpoint \
	vega/commands \
	vega/coreapi \
	vega/events \
	vega/oracles \
	vega/snapshot \
	vega/wallet
do
	touch "$generated_dir/$x/__init__.py"
done

find "$generated_dir/vega" -maxdepth 1 -name '*.py' -print0 | xargs -0r sed --in-place -r \
	-e 's#^from github.com.mwitkow.go_proto_validators #from ..github.com.mwitkow.go_proto_validators #' \
	-e 's#^from vega import ([a-z_]*)_pb2 as #from . import \1_pb2 as #' \
	-e 's#^from vega.commands.v1 import#from .commands.v1 import#' \
	-e 's#^from vega.coreapi.v1 import#from .coreapi.v1 import#' \
	-e 's#^from vega.events.v1 import#from .events.v1 import#' \
	-e 's#^from vega.oracles.v1 import#from .oracles.v1 import#' \
	-e 's#^from vega.snapshot.v1 import#from .snapshot.v1 import#' \
	-e 's#^from vega.wallet.v1 import#from .wallet.v1 import#' \
	-e 's#^import ([a-z_]*)_pb2 as #from . import \1_pb2 as #'

find "$generated_dir/vega/api" -maxdepth 1 -name '*.py' -print0 | xargs -0r sed --in-place -r \
	-e 's#^from github.com.mwitkow.go_proto_validators #from ...github.com.mwitkow.go_proto_validators #' \
	-e 's#^from vega import ([a-z_]*)_pb2 as#from .. import \1_pb2 as#' \
	-e 's#^from vega.api import #from . import #' \
	-e 's#^from vega.commands.v1 import#from ..commands.v1 import#' \
	-e 's#^from vega.coreapi.v1 import#from ..coreapi.v1 import#' \
	-e 's#^from vega.events.v1 import#from ..events.v1 import#' \
	-e 's#^from vega.oracles.v1 import#from ..oracles.v1 import#' \
	-e 's#^from vega.snapshot.v1 import#from ..snapshot.v1 import#' \
	-e 's#^from vega.wallet.v1 import#from ..wallet.v1 import#' \
	-e 's#^import ([a-z_]*)_pb2 as #from ... import \1_pb2 as #'

find \
	"$generated_dir/vega/checkpoint/v1" \
	"$generated_dir/vega/commands/v1" \
	"$generated_dir/vega/coreapi/v1" \
	"$generated_dir/vega/events/v1" \
	"$generated_dir/vega/oracles/v1" \
	"$generated_dir/vega/snapshot/v1" \
	"$generated_dir/vega/wallet/v1" \
	-maxdepth 1 -name '*.py' -print0 | xargs -0r sed --in-place -r \
	-e 's#^from github.com.mwitkow.go_proto_validators #from ....github.com.mwitkow.go_proto_validators #' \
	-e 's#^from vega import ([a-z_]*)_pb2 as#from ... import \1_pb2 as#' \
	-e 's#^from vega.(commands.v1|coreapi.v1|events.v1|oracles.v1|snapshot.v1|wallet.v1|github.com.mwitkow.go_proto_validators) import #from ...\1 import #' \
	-e 's#^import ([a-z_]*_pb2) as #from ... import \1 as #'

find \
	"$generated_dir/data_node/api/v1" \
	-maxdepth 1 -name '*.py' -print0 | xargs -0r sed --in-place -r \
	-e 's#^from github.com.mwitkow.go_proto_validators #from ....github.com.mwitkow.go_proto_validators #' \
	-e 's#^from vega import ([a-z_]*)_pb2 as#from ....vega import \1_pb2 as#' \
	-e 's#^from vega.(commands.v1|coreapi.v1|events.v1|oracles.v1|snapshot.v1|wallet.v1|github.com.mwitkow.go_proto_validators) import #from ....vega.\1 import #' \
	-e 's#^from data_node.(api.v1) import #from ...\1 import #'

find "$generated_dir" -name '*.py' -print0 | xargs -0r sed --in-place -re 's#[ \t]+$##'
