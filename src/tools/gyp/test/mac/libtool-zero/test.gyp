# Copyright (c) 2014 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'mylib',
      'type': 'static_library',
      'sources': [
        'mylib.c',
      ],
      'xcode_settings': {
        'ARCHS': [ 'i386', 'x86_64' ],
      },
    },
  ],
}